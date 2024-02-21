from tkinter import *

root = Tk()
root.title('022')

def show():
    myLabel=Label(root,text=vara.get()).pack()
    myLabel=Label(root,text=varb.get()).pack()
    myLabel=Label(root,text=varc.get()).pack()
    myLabel=Label(root,text=vard.get()).pack()


vara = IntVar()
varb = IntVar()
varc = IntVar()
vard = IntVar()


a = Checkbutton(root,text="Check this box", variable=vara).pack()
b = Checkbutton(root,text="Check this box", variable=varb).pack()
c = Checkbutton(root,text="Check this box", variable=varc).pack()
d = Checkbutton(root,text="Check this box", variable=vard).pack()



myButton = Button(root,text="show selection",command=show).pack()
root.mainloop()