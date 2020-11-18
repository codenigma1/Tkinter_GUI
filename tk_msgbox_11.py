from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title('Practice Window')
root.iconbitmap('D:/Vaibhav/TKinter Project/app/favicon.ico')

# askyesno
def popup6():
	response = messagebox.askyesno("This is my Popup!", "Hello World!")
	Label(root, text = response).pack()
	# if response == 1:
	# 	Label(root, text = "You Clicked on Yes!").pack()
	# else:
	# 	Label(root, text = "You Clicked on NO!").pack()

# askokcancel
def popup5():
	messagebox.askokcancel("This is my Popup!", "Hello World!")

# askquestion
def popup4():
	messagebox.askquestion("This is my Popup!", "Hello World!")

# showerror
def popup3():
	messagebox.showerror("This is my Popup!", "Hello World!")

# showwarning
def popup2():
	messagebox.showwarning("This is my Popup!", "Hello World!")


# This is the showinfo message box
def popup1():
	messagebox.showinfo("This is my Popup!", "Hello World!")


Button(root, text = "showinfo msg", command = popup1).pack(pady = 5)
Button(root, text = "showwarning msg", command = popup2).pack(pady = 5)
Button(root, text = "showerror msg", command = popup3).pack(pady = 5)
Button(root, text = "askquestion msg", command = popup4).pack(pady = 5)
Button(root, text = "askokcancel msg", command = popup5).pack(pady = 5)
Button(root, text = "askyesno msg", command = popup6).pack(pady = 5)

root.mainloop()