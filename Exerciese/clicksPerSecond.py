# just trying to make a clikcs per second program

from tkinter import *
import time

count = 0
time = 0

def click():
  if time == 0:
    global count
    count += 1
  else:
    print("You clicked", count, "times in 1 second!")

window = Tk()

button = Button(window,
                text="Click me as fast\nas you can!",
                command=click,
                fg="#00FF00",
                bg="black",
                font=("Times New Roman", 60))

button.pack()

window.mainloop()