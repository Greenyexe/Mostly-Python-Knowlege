from tkinter import *
from tkinter.ttk import *

def start():
  KB = 16431
  download = 0
  speed = 1
  while download < KB:
    bar["value"]+=(speed/KB)*100
    download += speed
    percent.set(str(int(download/KB*100))+"%")
    text.set(str(download)+"/"+str(KB)+" KB downloaded")
    window.update_idletasks()
  Label(window, 
        text="I just wasted your time", 
        font=("times new roman",50), 
        background="red", 
        foreground="black").pack()
    

window = Tk()

percent = StringVar()
text = StringVar()

bar = Progressbar(window, orient=HORIZONTAL, length=200)
bar.pack(pady=10)

percentLabel = Label(window, textvariable=percent).pack()
taskLabel = Label(window, textvariable=text).pack()

button = Button(window, text="Download", command=start).pack()

window.mainloop()