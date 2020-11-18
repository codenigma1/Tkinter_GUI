from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Practice Window')
# Favicon change of the Tkinter
root.iconbitmap('D:/Vaibhav/TKinter Project/app/favicon.ico')
# Opening the images in Tkinter 
img1 = ImageTk.PhotoImage(Image.open("skills/1.png"))
img2= ImageTk.PhotoImage(Image.open("skills/2.png"))
img3 = ImageTk.PhotoImage(Image.open("skills/3.png"))
img4 = ImageTk.PhotoImage(Image.open("skills/4.png"))
img5 = ImageTk.PhotoImage(Image.open("skills/5.png"))
img6 = ImageTk.PhotoImage(Image.open("skills/6.png"))
img7 = ImageTk.PhotoImage(Image.open("skills/7.png"))
img8 = ImageTk.PhotoImage(Image.open("skills/8.png"))
img9 = ImageTk.PhotoImage(Image.open("skills/scikit.png"))
img10 = ImageTk.PhotoImage(Image.open("skills/scipy.png"))
img11 = ImageTk.PhotoImage(Image.open("skills/Seaborn.png"))
img12 = ImageTk.PhotoImage(Image.open("skills/sql.png"))

image_list = [img1, img2, img3, img4, img5, img6, img7, img8, img9, img10, img11, img12]

status = Label(root, text = "Image 1 of " + str(len(image_list)), bd = 1, relief = SUNKEN, anchor = E)

# Set the attributes
my_label = Label(image = img1)
# Display the image in the Window
my_label.grid(row = 0, column = 0, columnspan = 3)



def forward(image_number):
	global my_label
	global button_forward
	global button_back

	my_label.grid_forget()
	my_label = Label(image = image_list[image_number - 1])
	# Create the widget
	button_forward = Button(root, text = ">>", command = lambda: forward(image_number + 1))
	button_back = Button(root, text = "<<", command = lambda: backward(image_number - 1))

	# Update status bar
	status = Label(root, text = "Image "+ str(image_number) + " of " + str(len(image_list)), bd = 1, relief = SUNKEN, anchor = E)
 
	if image_number == len(image_list) - 1:
		button_forward = Button(root, text = ">>", state = DISABLED)

	# Put the widget on the screen
	my_label.grid(row = 0, column = 0, columnspan = 3)
	button_back.grid(row = 1, column = 0)
	button_forward.grid(row = 1, column = 2)
	status.grid(row = 2, column = 0, columnspan = 3, sticky = W+E)

def backward(image_number):
	global my_label
	global button_forward
	global button_back

	my_label.grid_forget()
	my_label = Label(image = image_list[image_number - 1])

	# Create the widget
	button_forward = Button(root, text = ">>", command = lambda: forward(image_number + 1))
	button_back = Button(root, text = "<<", command = lambda: backward(image_number - 1))

	# Update Status bar
	status = Label(root, text = "Image "+ str(image_number) + " of " + str(len(image_list)), bd = 1, relief = SUNKEN, anchor = E)

	if image_number == 1:
		button_back = Button(root, text = "<<", state = DISABLED)

	# Put the widget on the screen
	my_label.grid(row = 0, column = 0, columnspan = 3)
	button_back.grid(row = 1, column = 0)
	button_forward.grid(row = 1, column = 2)
	status.grid(row = 2, column = 0, columnspan = 3, sticky = W+E)
# Add button widgets
button_back = Button(root, text = "<<", command = backward, state = DISABLED)
button_exit = Button(root, text = "End", command = root.destroy)
button_forward = Button(root, text = ">>", command = lambda: forward(2))

# Display button on the screen
button_back.grid(row = 1, column = 0)
button_exit.grid(row = 1, column = 1)
button_forward.grid(row = 1, column = 2, pady = 10)
status.grid(row = 2, column = 0, columnspan = 3, sticky = W+E)

  

# quit the program

# button_quit.pack()

root.mainloop()