from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('020')
root.geometry("200x500")
#add vertical bar
vertical = Scale(root,from_=0, to=200) # you can't type vertical = Scale(root,from_=0, to=200).pack()
vertical.pack()

#horizontal bar
horizotal = Scale(root,from_=0,to=400,orient=HORIZONTAL)
horizotal.pack()

my_label = Label(root,text=horizotal.get()).pack()

def slide():
    #whenevr you move the bar a label will be added
    my_label = Label(root,text=horizotal.get()).pack()
    #geometry will be change you move the scroll bar and click the button
    root.geometry(str(horizotal.get())+"x400")

my_btn = Button(root,text="Click",command=slide).pack()
root.mainloop()