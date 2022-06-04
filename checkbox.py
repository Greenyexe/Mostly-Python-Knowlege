from tkinter import * 

def display(): # function to display the checkbox value
  if(x.get()==1): # if checkbox is checked
    print("You agreed to the terms") # display the message
  else: # if checkbox is not checked
    print("You did not agree to the terms") # display the message

window = Tk() # create a window

person = PhotoImage(file="Maths person.png") # create a photo image

x = IntVar() # create an integer variable

check_button = Checkbutton(window, # create a check button
                          text="I agree to the terms and conditions", # set the text
                          font=("Times New Roman", 20), # set the font
                          fg="black", # set the foreground color
                          bg="white", # set the background color
                          activebackground="black", # set the active background color
                          activeforeground="white", # set the active foreground color 
                          selectcolor="red", # set the select color  
                          variable=x, # set the variable
                          onvalue=1, # set the on value
                          offvalue=0, # set the off value
                          command=display, # set the command
                          padx=25, # set the padx
                          pady=10, # set the pady
                          image=person, # set the image
                          compound=LEFT) # set the compound

check_button.pack() # pack the check button
window.mainloop() # run the window