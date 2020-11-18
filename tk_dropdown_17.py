from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Practice Window')
root.iconbitmap('D:/Vaibhav/TKinter Project/app/favicon.ico')
root.geometry("400x400") # size of window 400 by 400

# Drop Down Boxes

def collect():
	myLabel = Label(root, text = select.get()).pack()

options = [
	"Monday", 
	"Tuesday", 
	"Wednesday", 
	"Thusday", 
	"Friday",
	"Saturday"
]

select = StringVar()
select.set(options[0])
drop = OptionMenu(root, select, *options)


drop.pack()
myButton = Button(root, text = "Select", command = collect).pack()

root.mainloop()