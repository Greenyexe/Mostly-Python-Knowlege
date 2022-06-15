from tkinter import *
from tkinter import filedialog # submodule of tkinter

def openFile():
  filePath = filedialog.askopenfilename(initialdir="C:\\Users\\edite\\Desktop",
                                        title="Open a file",
                                        filetypes=(("text files", "*.txt"),
                                        ("All files", "*.*")))
  file = open(filePath, "r") # r stands for read
  print(file.read())
  file.close()

window = Tk()

button = Button(window, text="Open", command=openFile)
button.pack()

window.mainloop()