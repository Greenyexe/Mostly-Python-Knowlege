from tkinter import *
from tkinter import filedialog

#******************************************************************************

def saveFile():
  file = filedialog.asksaveasfile(initialdir="C:\\Users\\edite\\Desktop",
                                  defaultextension=".txt",
                                  filetypes=[("Text file", ".txt"),
                                            ("HTML file", ".html"),
                                            ("All files", ".*")])
  if file is not None: # if user quites the file explorer it won't die
    return
  filetext = str(text.get(1.0, END))
  #filetext = input("Enter text: ") # for console window user retrieval
  file.write(filetext)
  file.close()

#******************************************************************************

window = Tk()

#******************************************************************************

button = Button(window, text="Save", command=saveFile)
button.pack()

#******************************************************************************

text = Text(window)
text.pack()

#******************************************************************************

window.mainloop()