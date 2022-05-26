# just trying to make a clikcs per second program

from tkinter import *
import time

count = 0

def click():
  global count
  count += 1
  time.sleep(1)

window = Tk()

button = Button(window,
                text="Click me as fast as you can!",
                command=click,
                fg="#00FF00",
                bg="black",
                font=("Times New Roman", 40))

button.pack()

window.mainloop()