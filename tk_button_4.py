from tkinter import *

root = Tk()

def myClick():
	myLabel1 = Label(root, text = 'You have just clicked on button')
	myLabel1.pack()


# command method to call function whereas In general we call the function myClick() in python
myButton = Button(root, text = 'Click me!', command = myClick, fg = 'red', bg = 'pink')

myButton.pack()

root.mainloop()