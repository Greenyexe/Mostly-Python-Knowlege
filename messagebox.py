from tkinter import *
from tkinter import messagebox

def click():
#  messagebox.showinfo(title = "This is an info message box", message = "This is a message box")
#  while True:
#   messagebox.showwarning(title = "Warning!", message = "You have a virus")
#   messagebox.showerror(title = "Error!", message = "You have an error")
  if messagebox.askokcancel(title = "Are you sure?", message = "Are you sure you want to quit?"):
    print("You clicked ok")
  else:
    print("You clicked cancel")

window = Tk()

button = Button(window,
                text="Click Me!",
                command=click)
button.pack()

window.mainloop()