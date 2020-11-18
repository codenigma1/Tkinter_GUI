from tkinter import *

root = Tk()
root.title('Practice Window')
root.iconbitmap('D:/Vaibhav/TKinter Project/app/favicon.ico')
root.geometry("400x400") # size of window 400 by 400


# Label.config(): Change text dynamically
# .config() change any things at runtime


def something():
	my_label.config(text = "This is new text!!!", font = ("Helvetica", 12)) 
	root.config(bg = "pink")
	myButton.config(text = "Correct answer", fg = "Green", state = DISABLED, pady = 10)

global my_label
my_label = Label(root, text = "This is old text", font = ("Arial", 18))
my_label.pack(pady=10)


global myButton
myButton = Button(root, text = "Click me", command = something)
myButton.pack(pady=10)

root.mainloop()