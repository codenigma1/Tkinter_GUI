from tkinter import *
from random import randint
from tkinter import ttk

root = Tk()
root.title('Application: Rock, Paper, Scissors')
root.iconbitmap('D:/Vaibhav/TKinter Project/app/favicon.ico')
root.geometry("500x600")
# Change bg color to white
root.config(bg = "white")

# Define our images
main = PhotoImage(file = 'Images/all.png')
rock = PhotoImage(file = 'Images/rock.png')
paper = PhotoImage(file = 'Images/paper.png')
scissors = PhotoImage(file = 'Images/scissors.png')

# Add images to a list
image_list = [rock, paper, scissors]
 
# Pick random number between 0 and 2
pick_number = randint(0, 2)

# Throw up an image when the program start
user_label = Label(root, text = "Please pick your items", bg = "white", font = ("Arial", 10))
image_label = Label(root, image = main, bd = 0)
image_label.pack(pady=20)
user_label.pack()

# Create Spin Function
def spin():
	# Pick random number
	pick_number = randint(0, 2)
	# Show image
	image_label.config(image = image_list[pick_number])

	# 0 = Rock
	# 1 = Paper
	# 2 = Scissors

	# Convert Dropdown choice to a number
	if user_choice.get() == "Rock":
		user_choice_value = 0
	elif user_choice.get() == "Paper":
		user_choice_value = 1
	elif user_choice.get() == "Scissors":
		user_choice_value = 2

	# Determine who win or lose
	if user_choice_value == 0: # Rock
		if pick_number == 0:
			win_lose_label.config(text = "It's tie, Spin again...", fg = "orange")
		elif pick_number == 1:
			win_lose_label.config(text = "Paper Cover Rock, You Lose...", fg = "red")
		elif pick_number == 2:
			win_lose_label.config(text = "Rock Smashes Scissors, You Win!", fb = "green")

	if user_choice_value == 1: # Paper
		if pick_number == 0:
			win_lose_label.config(text = "Paper Cover Rock, You Win!", fg = "green")
		elif pick_number == 1:
			win_lose_label.config(text = "It's tie, Spin again...", fg = "orange")
		elif pick_number == 2:
			win_lose_label.config(text = "Scissors Cuts Paper, You Lose...", fg = "red")

	if user_choice_value == 2: # Scissors
		if pick_number == 0:
			win_lose_label.config(text = "Scissors Broken by Rock, You Lose...", fg = "red")
		elif pick_number == 1:
			win_lose_label.config(text = "Scissors Cuts Paper, You Win!", fg = "green")
		elif pick_number == 2:
			win_lose_label.config(text = "It's tie, Spin again...", fg = "orange")

# Make our choice
user_choice = ttk.Combobox(root, value = ("Rock", "Paper", "Scissors"))
user_choice.current(0)
user_choice.pack(pady=20)

# Create Spin Button 
spin_button = Button(root, text = "Spin!", command = spin, bg = "Black", fg = "white")
spin_button.pack(pady=10)


# Label for showing if you won or lost
win_lose_label = Label(root, text = "", bg = "white", font = ("Helvetica", 18)) 
win_lose_label.pack(pady = 20)




root.mainloop()