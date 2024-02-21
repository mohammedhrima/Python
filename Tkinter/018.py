#creat new window
from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("new window")

top = Toplevel()
A = Label(top,text="Hello world").pack()
mainloop()