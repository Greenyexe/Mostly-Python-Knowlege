# radio button = similar to check box but only one can be selected at a time (from a group of radio buttons)

from tkinter import *

food = ["pineapple", "apple", "orange", "banana"]

def order():
  if (x.get()==0):
    print("You ordered " + food[0])
  elif (x.get()==1):
    print("You ordered " + food[1])
  elif (x.get()==2):
    print("You ordered " + food[2])
  elif (x.get()==3):
    print("You ordered " + food[3])
  else:
    print("You did not order anything")

window = Tk()

#pineappleImage = PhotoImage(file="pineapple.png")
#appleImage = PhotoImage(file="apple.png")
#orangeImage = PhotoImage(file="orange.png")
#bananaImage = PhotoImage(file="banana.png")


x=IntVar()

for index in range(len(food)):
  radiobutton = Radiobutton(window, # create a radio button
                            text=food[index], # set the text
                            variable=x, #groups radiobuttons together if they share the same variable
                            value=index, #assigns each radiob utton a different value
                            padx=25, # set the padx
                            pady=10, # set the pady
                            font=("Impact", 50), # set the font")
                            #image=pineappleImage[index], # set the image)
                            #image=appleImage[index], # adds image to radiobutton
                            #image=orangeImage[index], 
                            #image=bananaImage[index], 
                            #compound=LEFT, # set the compound needed for images
                            indicatoron=0, # eliminates the tick mark
                            width = 10, # set the width of push buttons
                            command=order) # set the command
                            
  radiobutton.pack(anchor=W)

window.mainloop()