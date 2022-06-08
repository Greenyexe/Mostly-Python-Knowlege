# just trying to make a clikcs per second program

from tkinter import *
import time

#*****************************************************************************************

def callback():
  global timey
  timey = int(entrybox.get())
  print(timey)
  window.after(timey*1000, lambda: window.destroy())

#*****************************************************************************************

count = []

#*****************************************************************************************

window = Tk()

#*****************************************************************************************

entrybox = Entry(window,
                 width=15,
                 bg="pink",
                 fg="black",
                 font=("Arial", 50))
entrybox.pack()

#*****************************************************************************************

submit = Button(window,
                text="Submit",
                command=callback,
                font=("Arial", 20),
                bg="green",
                fg="black")
submit.pack()

#*****************************************************************************************

button = Button(window,
                text="Click me as fast\nas you can after\ninputing the time\non the entrybox above!",
                command=lambda: count.append(1),
                fg="#00FF00",
                bg="black",
                font=("Times New Roman", 60))
button.pack()

#*****************************************************************************************

window.mainloop()

#*****************************************************************************************

print("{} clicks in {} seconds".format(len(count), timey))