from tkinter import *

# grid() = geometry manager that organizes widgets in a table-like structure in a parent widget.

def submit():
  print("Brute force hacking your account... please wait")

window = Tk()

titleLabel = Label(window, text="Sign your life away:",font=("Arial",20)).grid(row=0,column=0,columnspan=2)

firstNameLabel = Label(window, text="First Name").grid(row=1,column=0)
firstNameEntry = Entry(window).grid(row=1,column=1)

lastNameLabel = Label(window, text="Last Name").grid(row=2,column=0)
lastNameEntry = Entry(window).grid(row=2,column=1)

emailLabel = Label(window, text="Email").grid(row=3,column=0)
emailEntry = Entry(window).grid(row=3,column=1)

submitButton = Button(window, text="Submit",command=submit).grid(row=4,column=0,columnspan=2)


window.mainloop()