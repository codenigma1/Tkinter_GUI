from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Practice Window')
root.iconbitmap('D:/Vaibhav/TKinter Project/app/favicon.ico')

# Fram sepearting thing out visually. it's good thing!
# Inside of padding of the frame
frame = LabelFrame(root, padx = 50, pady = 50)
# Outside of padding of the frame
frame.pack(padx = 20, pady = 20)

# Display
b = Button(frame, text = "Click me!")
b2 = Button(frame, text = "Don't click me!")
b.grid(row = 0, column = 0)
b2.grid(row = 0, column = 1)




root.mainloop()