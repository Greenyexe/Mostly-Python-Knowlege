from tkinter import *

# label = an area widget that holds text and/or an iage within a window

window = Tk()

photo = PhotoImage(file="Maths person.png")

label = Label(window,
        text="I've been\nwatching you!", 
        font = ("TimesNewRoman", 40, "bold"), 
        fg="green", 
        bg="black", 
        relief=RAISED,
        bd=10,
        padx=20,
        pady=20,
        image=photo,
        compound="top")

label.pack()
#label.place(x=100,y=100) # down by 100 pixels, to the right by 100 pixels

window.mainloop()