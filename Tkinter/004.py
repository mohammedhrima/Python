from tkinter import *
#boxy window or widget
root = Tk()

#disbaled button , hidden , like you don't have access to it
myButton1 = Button(root, text="Clique me 1",state=DISABLED)
myButton2 = Button(root, text="Clique me 2")
myButton3 = Button(root, text="Clique me 3", padx=50)
myButton4 = Button(root, text="Clique me 4", padx=50, pady=50)

#function
def Clique():
    myLabel = Label(root, text="Look! I clicked a Button!!!")
    myLabel.pack()

#fg frontground / bg background
myButton5 = Button(root, text="Clique me 5", command=Clique,padx=50, pady=25,fg = "red",bg = "blue")

#pack the function
myButton1.pack()
myButton2.pack()
myButton3.pack()
myButton4.pack()
myButton5.pack()

root.mainloop()