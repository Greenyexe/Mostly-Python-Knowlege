from tkinter import *

window = Tk()

label = Label(window,
              text="How would you rate\nyour expirence?",
              font=("TimesNewRoman", 20, "bold"),
              padx=20,
              pady=20,
              bg="pink",
              fg="blue")
label.pack()

scale = Scale(window,
              from_=10,
              to=0,
              length=600,
              orient=VERTICAL, # orient=VERTICAL is the default
              font=("Times New Roman", 20),
              tickinterval=1, # adds numeric labels to the scale
              #showvalue=0, #hide current value
              troughcolor="#69EAFF", # color of the scale
              fg="#FF1C00", # foreground color
              bg="pink", # background color
              ) 
scale.set(((scale["from"]-scale["to"])/2)+scale["to"]) # set the default value

scale.pack()

button = Button(window,text="Submit",command=lambda: print("The customer satisfation was " + str(scale.get())+" out of 10"), font=("Times New Roman", 20, "bold"))
button.pack()

window.mainloop()