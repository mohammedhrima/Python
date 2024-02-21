from tkinter import *
#boxy window or widget
root = Tk()

#Creating a label Widget and Showing it in the screen
mylabel1 = Label(root,text="Hello World!").grid(row=0,column=0)
mylabel2 = Label(root,text="My Name is John Elder").grid(row=1,column=5)

root.mainloop()