from tkinter import *
from tkinter import colorchooser # submodule of tkinter

def click():
#  colour = colorchooser.askcolor()
#  print(colour)
#  colourHex = colour[1]
#  print(colourHex)
#  window.config(bg=colourHex) # change background colour of window
  window.config(bg=colorchooser.askcolor()[1]) # change background colour of window

window = Tk()

window.geometry("400x400")

button = Button(window, text="click me", command=click)
button.pack()

window.mainloop()