from logging import root
from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

root = Tk()
root.title('File dialog')
"""
# for all files use ("all files","*.*")
root.filename = filedialog.askopenfilename(initialdir="/home/ironman/Desktop",title="Select a file",filetypes=(("png files","*.png"),("document",".doc"),("excel files",".xls"),("excel files",".xlsx"),("pdf files",".pdf"),("Images",".jpg"),("Images",".png"),("Images",".ico")))
#retrun the name of location
my_label = Label(root,text=root.filename).pack()
#open the image in the specifique location
my_image = ImageTk.PhotoImage(Image.open(root.filename))
my_image_label= Label(image=my_image).pack()
"""
def open():
    global my_image
    # for all files use ("all files","*.*")
    root.filename = filedialog.askopenfilename(initialdir="/home/ironman/Desktop",title="Select a file",filetypes=(("png files","*.png"),("document",".doc"),("excel files",".xls"),("excel files",".xlsx"),("pdf files",".pdf"),("Images",".jpg"),("Images",".png"),("Images",".ico")))
    #retrun the name of location
    my_label = Label(root,text=root.filename).pack()
    #open the image in the specifique location
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label= Label(image=my_image).pack()

My_btn = Button(root,text="Open File",command=open).pack()


root.mainloop()