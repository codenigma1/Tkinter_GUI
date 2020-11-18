from tkinter import *

root = Tk()

# Creating the widget
myLabel = Label(root, text = 'Hello world!')

# Packing the widget 
myLabel.pack()

# mainloop() tells Python to run the Tkinter event loop. it's run the code until it's clsoed
root.mainloop()