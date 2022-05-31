# just trying to make a clikcs per second program

from tkinter import *
import time

count = 0
time = 0
tEnd = time.time() + 1 *1

def click():
  while time.time() < tEnd:
    count += 1
  print("You clicked", count,"times in a second")
window = Tk()

button = Button(window,
                text="Click me as fast\nas you can!",
                command=click,
                fg="#00FF00",
                bg="black",
                font=("Times New Roman", 60))

button.pack()

window.mainloop()