from tkinter import *

def open_file():
  print("A file has been opened")
def save_file():
  print("A file has been saved")
def cut():
  print("Text has been cut")
def copy():
  print("Text has been copied")
def paste():
  print("Text has been pasted")

window = Tk()

#openImage = PhotoImage(file="open.png")
#saveImage = PhotoImage(file="save.png")
#exitImage = PhotoImage(file="exit.png")

menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar,tearoff=0,font=("MV Boli",10))
menubar.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label="Open",command=open_file)#,image=openImage,compound=LEFT)
fileMenu.add_command(label="Save",command=save_file)#,image=saveImage,compound=LEFT)
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=quit)#,image=exitImage,compound=LEFT)

editMenu = Menu(menubar,tearoff=0,font=("MV Boli",10))
menubar.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="Cut",command=cut)
editMenu.add_command(label="Copy",command=copy)
editMenu.add_command(label="Paste",command=paste)

window.mainloop()