# just trying to make a clikcs per second program

from tkinter import *
import time

count = []
time = int(input("How long do you want to have to click for (in seconds)?\n: "))

window = Tk()

button = Button(window,
                text="Click me as fast\nas you can!",
                command=lambda: count.append(1),
                fg="#00FF00",
                bg="black",
                font=("Times New Roman", 60))

button.pack()

window.after(time*1000, lambda: window.destroy())

window.mainloop()

print("{} clicks in {} seconds".format(len(count), time))