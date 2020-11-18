from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title('Practice Window')
root.iconbitmap('D:/Vaibhav/TKinter Project/app/favicon.ico')
root.geometry("400x400") # size of window 400 by 400

vertical = Scale(root, from_ = 0, to = 400)
vertical.pack()

def slide(var):
	my_label = Label(root, text = horizontal.get()).pack()
	root.geometry((str(horizontal.get()) + "x400"))

horizontal = Scale(root, from_ = 0, to = 400, orient = HORIZONTAL, command = slide)
horizontal.pack()

my_label = Label(root, text = horizontal.get()).pack()

btn = Button(root, text = "Click Here!", command = slide).pack()

root.mainloop()