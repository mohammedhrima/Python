from tkinter import *
#boxy window or widget
root = Tk()

#Window to enter an input
#bg : the background , fg : the font 
e = Entry(root,width=50, bg ="green",fg="red",borderwidth=4)
e.pack()
e.insert(0, "Enter your Name: ")

def myClick():
    hello = "Hello "+ e.get()
    A = Label(root,text="Good!"+hello)
    A.pack()

#creat a button
B = Button(root,text="clique me",padx=30,pady=20,command=myClick)
B.pack()


root.mainloop()