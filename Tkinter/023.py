from tkinter import *

root = Tk()
root.title('022')

def show():
    myLabel=Label(root,text=var.get()).pack()
 


var = StringVar()


a = Checkbutton(root,text="Check this box", variable=var,onvalue="On",offvalue="Off")
a.deselect() #to desable autocheck value
a.pack()

myButton = Button(root,text="show selection",command=show).pack()
root.mainloop()