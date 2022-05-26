from tkinter import *

# button = you click it, then it does stuff

count = 0
def click():
  global count
  print("You clicked the button")
  count +=1
  print(count)

window = Tk()

photo = PhotoImage(file="Maths person.png")

button = Button(window,
                text="Click me!",
                command=click,
                font=("Comic Sans", 32),
                fg="green",
                bg="black",
                activeforeground="green",
                activebackground="black",
                state=ACTIVE,
                image=photo,
                compound="bottom") # can say disabled saying its active is not nessasary
button.pack()

window.mainloop()