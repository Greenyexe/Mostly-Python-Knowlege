from tkinter import *

def create_window():
  new_window = Tk() # Toplevel() = new window 'on top' of other windows, linked to a 'bottom' window
                    # Tk() = new inderpendent window, not linked to any other window
  old_window.destroy() # destroy() = close window

old_window = Tk()

Button(old_window,text="Create new window",command=create_window).pack()

old_window.mainloop()