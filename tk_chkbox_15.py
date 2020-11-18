from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Practice Window')
root.iconbitmap('D:/Vaibhav/TKinter Project/app/favicon.ico')
root.geometry("400x400") # size of window 400 by 400

# var = IntVar()
var = StringVar()

c = Checkbutton(root, text = "Chk Box", variable = var, onvalue = "On", offvalue = "Off")
c.deselect()
c.pack()

# myLabel = Label(root, text = var.get()).pack()

def check():
	myLabel = Label(root, text = var.get()).pack()

btn = Button(root, text = "Check Selection", command = check).pack()

root.mainloop()