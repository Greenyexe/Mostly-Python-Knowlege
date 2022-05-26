from tkinter import *

# widgets = GUI elements: buttons, textboxes, labels, images
# windows = serves as a container to hold or contain these widgets

window = Tk() # instantiate an instance of a window
window.geometry("420x420")
window.title("I am cool")

icon = PhotoImage(file="Maths person.png")
window.iconphoto(True, icon)
window.config(background="#5cfcff") # can also just type the name of a colour e.g. "black" 

window.mainloop() # place window on computer screen, listen for events