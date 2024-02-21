# Import the required libraries
from tkinter import *

# Create an instance of tkinter frame or window
win=Tk()

# Set the size of the tkinter window
win.geometry("700x350")

def cal_sum():
   t1=int(a.get())
   t2=int(b.get())
   sum=t1+t2
   label.config(text=sum)

# Create an Entry widget
Label(win, text="Enter First Number", font=('Calibri 10')).pack()
a=Entry(win, width=35)
a.pack()
Label(win, text="Enter Second Number", font=('Calibri 10')).pack()
b=Entry(win, width=35)
b.pack()

label=Label(win, text="Total Sum : ", font=('Calibri 15'))
label.pack(pady=20)

Button(win, text="Calculate Sum", command=cal_sum).pack()

win.mainloop()