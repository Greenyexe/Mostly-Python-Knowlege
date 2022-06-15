# text widget = functions like a text area, you can entry multiple lines of text
from tkinter import *

window = Tk()

text = Text(window,
            bg="lightyellow",
            font=("Ink Free", 15),
            height=15,
            width=40,
            padx=20,
            pady=20,
            fg="purple")
text.pack()

button = Button(window, text="Submit", command=lambda:print(text.get("1.0", END)))
button.pack()

window.mainloop()