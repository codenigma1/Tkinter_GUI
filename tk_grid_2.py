from tkinter import *

root = Tk()

# Creating the widget; making the something
myLabel1 = Label(root, text = 'Hello world!')
myLabel2 = Label(root, text = 'My Name is Vaibhav Khobragade!')
myLabel3 = Label(root, text = '             ')


# Puting thing on the screen
# Griding the widget; row and columns form
myLabel1.grid(row = 0, column = 0)
myLabel2.grid(row = 1, column = 1)
myLabel3.grid(row = 3, column = 4)

# mainloop() tells Python to run the Tkinter event loop. it's run the code until it's clsoed
root.mainloop()