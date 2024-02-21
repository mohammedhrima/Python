from tkinter import *
#boxy window or widget
root = Tk()

#creating a Label Widget
myLabel1  = Label(root, text="Hello World")
myLabel2  = Label(root, text="My name is mohammed")
myLabel3  = Label(root, text="Hope you are fine")

# Shoving it into the screen
#grid used to specify where you want to put the text
#the text doesn't stay in the midle like pack()
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1,column=1)
myLabel3.grid(row=2,column=5) #the number ar relative like one after another
root.mainloop()

