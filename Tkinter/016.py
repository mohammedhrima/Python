from tkinter import *
from PIL import ImageTk,Image


root = Tk()
root.title('Radio buttons')

#to keep tracking the varibale r
r = IntVar()
#there is set and get
r.set("2")

MODES = [
    ("Pepperoni","Pepperoni"),
    ("Cheese","Cheese"),
    ("Mushroom","Mushroom"),
    ("Onion","Onion"),
]

pizza = StringVar()

pizza.set(" ")

for text,mode in MODES:
    #anchor=W to move text to the left
    Radiobutton(root,text=text,variable=pizza,value=mode).pack(anchor=W)


def Clicked(value):
    myLabel = Label(root,text=value)
    myLabel.pack()

#Radiobutton(root,text="Option 1",variable=r,value=1,command=lambda:Clicked(r.get())).pack()
#Radiobutton(root,text="Option 2",variable=r,value=2,command=lambda:Clicked(r.get())).pack()

#myLabel = Label(root,text=pizza.get())
#myLabel.pack()

myButton = Button(root,text="Click Me!",command=lambda:Clicked(pizza.get()))
myButton.pack()

mainloop()