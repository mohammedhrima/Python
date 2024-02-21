from tkinter import *

root = Tk()

e = Entry(root, width=50)
e.pack()
#take input from user
e.insert(0,"Enter your name: ")

def myClick():
    hello = "Hello " + e.get()
    mylabel = Label(root, text = hello)
    mylabel.pack()

myButton = Button(root, text="Clique me", command=myClick)
myButton.pack()

root.mainloop()