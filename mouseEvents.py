from tkinter import *

def dosomething(event):
  print("Mouse coordinates: "+str(event.x)+","+str(event.y))

window = Tk()

#window.bind("<Button-1>", dosomething) # Left mouse button
#window.bind("<Button-2>", dosomething) # Middle mouse button
#window.bind("<Button-3>", dosomething) # Right mouse button
#window.bind("<ButtonRelease>", dosomething)
#window.bind("<Enter>", dosomething) # Mouse enters window
#window.bind("<Leave>", dosomething) # Mouse leaves window
window.bind("<Motion>", dosomething) # Where the mouse moved

window.mainloop()