import numpy as np
import cv2
from PIL import Image
import PIL

prototxt_path  = '.hide/tools/colorization_deploy_v2.prototxt'
model_path = '.hide/tools/colorization_release_v2.caffemodel'
kernel_path = '.hide/tools/pts_in_hull.npy'
image_path = '004.jpg'

list =("003.jpeg","004.jpg","005.jpg","006.jpg","007.jpg")



def Img_conv():
    net = cv2.dnn.readNetFromCaffe(prototxt_path, model_path)
    points = np.load(kernel_path)

    points = points.transpose().reshape(2,313,1,1)

    net.getLayer(net.getLayerId("class8_ab")).blobs = [points.astype(np.float32)]
    net.getLayer(net.getLayerId("conv8_313_rh")).blobs = [np.full([1,313],2.606,dtype="float32")]

    bw_image = cv2.imread(image_path)
    #bw_image = cv2.resize(bw_image,(244,244))
    normalized = bw_image.astype("float32")/255.0
    lab = cv2.cvtColor(normalized,cv2.COLOR_BGR2LAB)

    #244x244
    resized = cv2.resize(lab,(244,244))
    L = cv2.split(resized)[0]
    L -= 50

    net.setInput(cv2.dnn.blobFromImage(L))
    ab = net.forward()[0,:,:,:].transpose((1,2,0))
    ab = cv2.resize(ab,(bw_image.shape[1],bw_image.shape[0]))
    L = cv2.split(lab)[0]
    colorized = np.concatenate((L[:,:,np.newaxis],ab),axis=2)
    colorized = cv2.cvtColor(colorized,cv2.COLOR_LAB2BGR)
    colorized = (255.0 * colorized).astype("uint8")

    
    #colorized = cv2.resize(colorized,(244,244))
    x = image_path[0:3] + '-1.jpg'
    #cv2.imwrite(x,colorized)
    #"""
    img1 = bw_image
    img2 = colorized

    vis = np.concatenate((img1, img2), axis=1)
    #vis = cv2.resize(vis,(500,500))
    x = image_path[0:3] + '-2.jpg'
    cv2.imwrite(x,vis)
    #cv2.imshow('out.png', vis)
    a = cv2.imread(x)
    h,w = a.shape[:2]
    a = cv2.resize(a, (round(w / 2), round(h / 2)), interpolation=cv2.INTER_AREA)
    #cv2.imshow("DD",a)
    #cv2.waitKey()
    #cv2.destroyAllWindows()
    #"""

for x in list:
    image_path = x
    Img_conv()