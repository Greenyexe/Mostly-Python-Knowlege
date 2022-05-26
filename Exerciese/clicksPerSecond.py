# just trying to make a clikcs per second program

from tkinter import *
import time

count = 0

def click():
  global count

window = Tk()

button = Button(window,
                text="Click me as fast as you can!",
                command=click,)