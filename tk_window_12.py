from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title('Practice Window')
root.iconbitmap('D:/Vaibhav/TKinter Project/app/favicon.ico')

# Open second window by clicking button

def open():
	global img
	top = Toplevel()
	top.title('Second Window')
	img = ImageTk.PhotoImage(Image.open("alien.png"))
	my_label = Label(top, image = img).pack()
	btn2 = Button(top, text = "Close", command = top.destroy).pack()


btn = Button(root, text = "Second Window", command = open).pack()

root.mainloop()