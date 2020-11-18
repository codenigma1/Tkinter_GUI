from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Practice Window')
# Favicon change of the Tkinter
root.iconbitmap('D:/Vaibhav/TKinter Project/app/favicon.ico')
# Adding the image in Tkinter
img = ImageTk.PhotoImage(Image.open("alien.png"))
my_label = Label(image = img)

# Display the image in the window
my_label.pack()
 

# quit the program
button_quit = Button(root, text="Exit Program", 
	command = root.quit)

button_quit.pack()

root.mainloop()