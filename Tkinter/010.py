from tkinter import *
from tkinter.ttk import *
from PIL import Image,ImageTk

root = Tk()
root.title("Learn to code")
#linux doesn't support jpg files
#so you have to convert it to gif by usine that
img = Image.open("009.jpg")
img.save("009.gif")
img = PhotoImage(file='009.gif')
root.iconphoto(False,img)
#import image
my_img1 = Image.open("010-1.jpeg")
my_img2 = Image.open("010-2.jpeg")
my_img3 = Image.open("010-3.jpg")
my_img4 = Image.open("010-4.jpg")
my_img5 = Image.open("010-5.jpeg")

i=0
image_list = [my_img1,my_img2,my_img3,my_img4,my_img5]
img_selected = image_list[i]
def forw():
    global i
    if i < len(image_list)-1:
        i = i +1
    else:
        i = 0
    global img_selected
    img_selected = image_list[i].resize((800,450),Image.ANTIALIAS)
    img_selected = ImageTk.PhotoImage(img_selected)
    global my_label
    my_label = Label(image=img_selected).grid(row=0,column=0,columnspan=3)
def bac():
    global i
    if i > 0:
        i = i -1
    else:
        i = len(image_list)-1
    global img_selected
    img_selected = image_list[i].resize((800,450),Image.ANTIALIAS)
    img_selected = ImageTk.PhotoImage(img_selected)
    global my_label
    my_label = Label(image=img_selected).grid(row=0,column=0,columnspan=3)

forw()
bac()

my_label = Label(image=img_selected).grid(row=0,column=0,columnspan=3)

button_quit = Button(root,text="Exit",command=root.quit).grid(row=1,column=1)
forward = Button(root,text=">>",command=forw).grid(row=1,column=2)
back = Button(root,text="<<",command=bac).grid(row=1,column=0)


root.mainloop()