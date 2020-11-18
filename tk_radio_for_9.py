from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Practice Window')
root.iconbitmap('D:/Vaibhav/TKinter Project/app/favicon.ico')

pizza = StringVar()
pizza.set("Pepperoni")
 

def clicked(value):
	myLabel = Label(root, text = value)
	myLabel.pack()

# Tuples
toppings = [

	("Pepperoni","Pepperoni"),
	("Cheese","Cheese"),
	("Mushroom","Mushroom"),
	("Onion","Onion"),

]

for text, topping in toppings:
	Radiobutton(root, text = text, variable = pizza, value = topping).pack()


myButton = Button(root, text = "Click me!", command = lambda: clicked(pizza.get()))

myButton.pack()



root.mainloop()