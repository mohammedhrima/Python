from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Learn to code')

img = Image.open('013.ico')
img.save('013.gif')
img = PhotoImage(file='013.gif')
root.iconphoto(False,img)

#declare variable in tkinter as intiger with IntVar , and StrVar for strings
r = IntVar()
r.set("2")

def clicked(value):
    myLabel = Label(root, text= value)
    myLabel.pack()
Radiobutton(root,text="option 1",variable=r,value=1, command=lambda: clicked(r.get())).pack()
Radiobutton(root,text="option 2",variable=r,value=2,command=lambda: clicked(r.get())).pack()

myLabel = Label(root, text = r.get()).pack()
myButton = Button(root, text=)
mainloop()