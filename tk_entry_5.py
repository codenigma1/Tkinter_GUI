from tkinter import *

root = Tk()

# This is the input box or entry widget 
e = Entry(root, width = 30, bg = 'Gray', fg = 'white', borderwidth = 3)
e.pack()
e.insert(0, "Enter your stock quote") # Placeholder

# Function
def myClick():
	hello = 'Hello '+ e.get()
	myLabel1 = Label(root, text = hello)
	myLabel1.pack()


# command method to call function whereas In general we call the function myClick() in python
myButton = Button(root, text = 'Click me!', command = myClick, fg = 'red', bg = 'pink')

myButton.pack()

root.mainloop()