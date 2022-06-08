# listbox = A listing of selectable text items within it's own container

#******************************************************************************

from tkinter import *

#******************************************************************************

def submit():
  food = []

  for index in listbox.curselection(): 
    food.insert(index, listbox.get(index)) # get the selected item
  
  print("You have ordered:")

  for item in food:
    print(item)

#  print("You have ordered {}".format(listbox.get(listbox.curselection())))

#******************************************************************************

def add():
  listbox.insert(listbox.size(), entrybox.get()) 
  listbox.config(height=listbox.size())

#******************************************************************************

def delete(): 
#  listbox.delete(listbox.curselection())

  for index in reversed(listbox.curselection()): # need to reverse the order
    listbox.delete(index)

  listbox.config(height=listbox.size())

#******************************************************************************

window = Tk()

#******************************************************************************

listbox = Listbox(window,
                  bg = "yellow",
                  fg = "black",
                  font = ("Constantia", 32),
                  width = 12,
                  selectmode = MULTIPLE)
listbox.pack()  

listbox.insert(1,"pizza")
listbox.insert(2,"burger")
listbox.insert(3,"chicken")
listbox.insert(4,"salad")
listbox.insert(5,"soup")

listbox.config(height = listbox.size())

#******************************************************************************

entrybox = Entry(window)
entrybox.pack()

#******************************************************************************

submit = Button(window,text = "Submit",command=submit)
submit.pack()

#******************************************************************************

addButton = Button(window,text = "Add",command=add)
addButton.pack()

#******************************************************************************

deleteButton = Button(window,text = "Delete",command=delete)
deleteButton.pack()

#******************************************************************************

window.mainloop()