from tkinter import *
from tkinter import messagebox

def click():
#  messagebox.showinfo(title = "This is an info message box", message = "This is a message box")
#  while True:
#   messagebox.showwarning(title = "Warning!", message = "You have a virus")
#   messagebox.showerror(title = "Error!", message = "You have an error")
#  if messagebox.askokcancel(title = "Are you sure?", message = "Are you sure you want to quit?"):
#    print("You clicked ok")
#  else:
#    print("You clicked cancel")
#  if messagebox.askretrycancel(title = "Retry?", message = "Do you want to retry?"):
#    print("You clicked retry")
#  else:
#    print("You clicked cancel")
#  if messagebox.askyesno(title = "Yes or No?", message = "Do you want to continue?"):
#    print("You clicked yes")
#  else:
#    print("You clicked no")
#  answer = messagebox.askquestion(title = "Question", message = "Do you want to continue?")
#  if answer == "yes":
#    print("You clicked yes")
#  else:
#    print("You clicked no")
  answer = messagebox.askyesnocancel(title = "Question", message = "Do you like to code?",icon = "question")
  if answer==True:
    print("You like to code")
  elif answer==False:
    print("You don't like to code")
  else:
    print("You don't want to answer")


window = Tk()

button = Button(window,
                text="Click Me!",
                command=click)
button.pack()

window.mainloop()