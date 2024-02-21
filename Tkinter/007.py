from tkinter import *

root = Tk()
#name of app
root.title("Simple Calculator")
#the screen
e = Entry(root, width=20,borderwidth=0)
#row = 1st line , colum = 1st colum , columspan = has the width of 3 buttons
e.grid(row=0,column=0,columnspan=3, padx=20,pady=5)


def click(number):
    #delet what's already in the screen (the box)
    #e.delete(0,END)num
    current = e.get()
    e.delete(0,END)
    e.insert(0, str(current) + str(number))

def Button_clear():
    e.delete(0,END)

def Button_add():
    first_number = e.get() 
    global f_num
    f_num = int(first_number)
    global operation
    operation = "+"
    e.delete(0,END)

def Button_multiply():
    first_number = e.get() 
    global f_num
    f_num = int(first_number)
    global operation
    operation = "*"
    e.delete(0,END)

def Button_subtract():
    first_number = e.get() 
    global f_num
    f_num = int(first_number)
    global operation
    operation = "-"
    e.delete(0,END)

def Button_divide():
    first_number = e.get() 
    global f_num
    f_num = int(first_number)
    global operation
    operation = "/"
    e.delete(0,END)

def Button_eq():
    second_number = int(e.get())
    e.delete(0,END)
    if operation == "+":
        e.insert(0, f_num+int(second_number))
    if operation == "-":
        e.insert(0, f_num-int(second_number))
    if operation == "/":
        e.insert(0, f_num/int(second_number))
    if operation == "*":
        e.insert(0, f_num*int(second_number))
    

#define buttons
Button1 = Button(root,padx=30, pady=20, command=lambda: click(1), text=1)
Button2 = Button(root,padx=30, pady=20, command=lambda: click(2), text=2)
Button3 = Button(root,padx=30, pady=20, command=lambda: click(3), text=3)
Button4 = Button(root,padx=30, pady=20, command=lambda: click(4), text=4)
Button5 = Button(root,padx=30, pady=20, command=lambda: click(5), text=5)
Button6 = Button(root,padx=30, pady=20, command=lambda: click(6), text=6)
Button7 = Button(root,padx=30, pady=20, command=lambda: click(7), text=7)
Button8 = Button(root,padx=30, pady=20, command=lambda: click(8), text=8)
Button9 = Button(root,padx=30, pady=20, command=lambda: click(9), text=9)
Button0 = Button(root,padx=30, pady=20, command=lambda: click(0), text=0)
Button_add = Button(root,text="+",padx=30,pady=20, command=Button_add)
Button_eq = Button(root,text="=",padx=60,pady=20, command=Button_eq)
Button_clear = Button(root,text="C",padx=30,pady=20, command=Button_clear)
Button_multiply = Button(root,text="*",padx=30,pady=20, command=Button_multiply)
Button_subtract = Button(root,text="-",padx=30,pady=20, command=Button_subtract)
Button_divide = Button(root,text="/",padx=30,pady=20, command=Button_divide)
Button1.grid(row=3,column=0)
Button2.grid(row=3,column=1)
Button3.grid(row=3,column=2)
Button4.grid(row=2,column=0)
Button5.grid(row=2,column=1)
Button6.grid(row=2,column=2)
Button7.grid(row=1,column=0)
Button8.grid(row=1,column=1)
Button9.grid(row=1,column=2)
Button0.grid(row=4,column=1)

Button_clear.grid(row=4,column=2, columnspan=2)
Button_add.grid(row=4, column=0)
Button_eq.grid(row=6 ,column=0, columnspan=2)
Button_multiply.grid(row=5,column=0)
Button_subtract.grid(row=5,column=1)
Button_divide.grid(row=5,column=2)


root.mainloop()
