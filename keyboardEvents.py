from tkinter import *

def dosomething(event):
#  print("You pressed:", event.keysym)
  label.config(text=event.keysym)

window = Tk()

window.bind("<Key>", dosomething)

label = Label(window,font=("Helvetica",100))
label.pack()

window.mainloop()