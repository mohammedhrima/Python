from tkinter import *
from tkinter.ttk import *
from PIL import Image,ImageTk

root = Tk()
root.title("Learn to code")
#linux doesn't support jpg files
#so you have to convert it to gif by usine that
img = Image.open("009.jpg")
img.save("009.gif")
img = PhotoImage(file='009.gif')
root.iconphoto(False,img)
#import image
my_img = ImageTk.PhotoImage(Image.open("009.jpg"))
my_label = Label(image=my_img).pack()

#to close the root
button_quit = Button(root,text="Exit",command=root.quit).pack()


root.mainloop()