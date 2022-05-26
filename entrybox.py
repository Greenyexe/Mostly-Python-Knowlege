from tkinter import *


# entry widget = textbox that accepts a single line of user input


def submit():
  username = entry.get()
  print("Hello "+username)
#  entry.config(state=DISABLED)

def delete():
  entry.delete(0,END)

def back():
  entry.delete(len(entry.get())-1,END)


window = Tk()


entry = Entry(window,
              font=("Times New Roman", 50),
#              show="*",
              fg="#00FF00",
              bg="black")
#entry.insert(0, "Username: ")
entry.pack(side=LEFT)


clearButton = Button(window, text="Clear",command=delete, font=("Comic Sans", 15), bg="green")
clearButton.pack(side=RIGHT)

backspaceButton = Button(window, text="Backspace",command=back, font=("Comic Sans", 15), bg="green")
backspaceButton.pack(side=RIGHT)

submitButton = Button(window, text="Submit",command=submit, font=("Comic Sans", 30), bg="green")
submitButton.pack(side=RIGHT)


window.mainloop()