from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()
root.title('Learn To code at Codemy.com')

def popup():
    messagebox.showinfo("this is my Popup!","hello")

Button(root,text="Popup",command=popup).pack()

mainloop()

