# frame = a rectangular containter to group and hold widgets

from tkinter import *

window = Tk()

frame = Frame(window,bg="pink",bd=5,relief=SUNKEN)
frame.place(x=0,y=0)

Button(frame,text="W",font=("Consolas",20),width=3).pack(side=TOP)
Button(frame,text="A",font=("Consolas",20),width=3).pack(side=LEFT)
Button(frame,text="S",font=("Consolas",20),width=3).pack(side=LEFT)
Button(frame,text="D",font=("Consolas",20),width=3).pack(side=LEFT)

window.mainloop()