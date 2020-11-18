from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title('Practice Window')
root.iconbitmap('D:/Vaibhav/TKinter Project/app/favicon.ico')


# initialdir set none it will open default directory
# It returns a path 
# root.filename = filedialog.askopenfilename(initialdir = "", title = "Select a file", filetypes = (("png files", "*.png"), ("all files", "*.*")))

# path = Label(root, text = root.filename).pack() 

# print(root.filename)
def open():
	global img
	root.filename = filedialog.askopenfilename(initialdir = "", title = "Select a file", filetypes = (("png files", "*.png"), ("all files", "*.*")))

	path = Label(root, text = root.filename).pack() 
	img = ImageTk.PhotoImage(Image.open(root.filename))
	img_label = Label(image = img).pack()


# it return the path
# myLabel = Label(root, text = root.filename).pack()
btn = Button(root, text = "Open file", command = open).pack()

root.mainloop()