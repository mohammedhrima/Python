from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Import frames')

img = Image.open('013.ico')
img.save('013.gif')
img = PhotoImage(file='013.gif')
root.iconphoto(False,img)
frame = LabelFrame(root, text="This is my frame", padx=50, pady=50)
frame.pack(padx=10,pady=10)

a = Button(frame, text="Don't Click Here !")
b = Button(frame, text="... or here !")
a.grid(row=0,column=0)
b.grid(row=1,column=1)

root.mainloop()
