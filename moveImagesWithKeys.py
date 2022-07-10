from tkinter import *

"""
def move_up(event):
  label.place(x=label.winfo_x(), y=label.winfo_y()-5)

def move_down(event):
  label.place(x=label.winfo_x(), y=label.winfo_y()+5)

def move_left(event):
  label.place(x=label.winfo_x()-5, y=label.winfo_y())

def move_right(event):
  label.place(x=label.winfo_x()+5, y=label.winfo_y())

window = Tk()
window.geometry("500x500")
window.configure(background="white")

window.bind("<w>",move_up)
window.bind("<a>",move_left)
window.bind("<s>",move_down)
window.bind("<d>",move_right)

window.bind("<Up>",move_up)
window.bind("<Left>",move_left)
window.bind("<Down>",move_down)
window.bind("<Right>",move_right)

maths = PhotoImage(file="Maths person.png")
label = Label(window, image=maths, relief=FLAT)
label.place(x=0, y=0)

window.mainloop()

# ^ Used to move image in a label
"""

def move_up(event):
  canvas.move(myimage,0,-5)

def move_down(event):
  canvas.move(myimage,0,5)

def move_left(event):
  canvas.move(myimage,-5,0)

def move_right(event):
  canvas.move(myimage,5,0)

window = Tk()

window.bind("<w>",move_up)
window.bind("<a>",move_left)
window.bind("<s>",move_down)
window.bind("<d>",move_right)

window.bind("<Up>",move_up)
window.bind("<Left>",move_left)
window.bind("<Down>",move_down)
window.bind("<Right>",move_right)

canvas = Canvas(window, width=500, height=500)
canvas.pack()

maths = PhotoImage(file="Maths person.png")
myimage = canvas.create_image(0, 0, image=maths, anchor=NW)

window.mainloop()