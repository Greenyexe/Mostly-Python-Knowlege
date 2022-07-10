from tkinter import *
from ball import *
import time

window = Tk()

WIDTH = 750 
HEIGHT = 750

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

volley_ball = Ball(canvas,0,0,100,1,6,"white")
tennis_ball = Ball(canvas,0,0,50,4,3,"yellow")
basketball_ball = Ball(canvas,0,0,125,8,7,"orange")
red_ball = Ball(canvas,0,0,90,6,5,"red")
blue_ball = Ball(canvas,0,0,150,4,2,"blue")
green_ball = Ball(canvas,0,0,75,10,8,"green")

while True:
  volley_ball.move()
  tennis_ball.move()
  basketball_ball.move()
  red_ball.move()
  blue_ball.move()
  green_ball.move()
  window.update()
  time.sleep(0.01)

window.mainloop()