# Why is this so satisfying?

from tkinter import *
import time

class Ball:

  def __init__(self,canvas,x,y,diameter,diameter2,xVelocity,yVelocity,color):
    self.canvas = canvas
    self.image = canvas.create_oval(x,y,diameter,diameter2,fill=color)
    self.xVelocity = xVelocity
    self.yVelocity = yVelocity

  def move(self):
    coordinates = self.canvas.coords(self.image)
    print(coordinates)
    if (coordinates[2] >= (self.canvas.winfo_width()) or coordinates[0]<0):
      self.xVelocity = -self.xVelocity

    if (coordinates[3] >= (self.canvas.winfo_height()) or coordinates[1]<0):
      self.yVelocity = -self.yVelocity


    self.canvas.move(self.image,self.xVelocity,self.yVelocity)

window = Tk()

WIDTH = 750 
HEIGHT = 750

canvas = Canvas(window,width=WIDTH,height=HEIGHT,background="black")
canvas.pack()

volley_ball = Ball(canvas,0,0,100,100,1,6,"white")
tennis_ball = Ball(canvas,0,0,50,50,4,3,"yellow")
basketball_ball = Ball(canvas,0,0,125,125,8,7,"orange")
red_ball = Ball(canvas,0,0,90,90,6,5,"red")
blue_ball = Ball(canvas,0,0,150,150,4,2,"blue")
green_ball = Ball(canvas,0,0,75,75,10,8,"green")
purple_ball = Ball(canvas,350,0,425,75,0,8,"purple")
pink_ball = Ball(canvas,0,0,20,20,20,15,"pink")

while True:
  volley_ball.move()
  tennis_ball.move()
  basketball_ball.move()
  red_ball.move()
  blue_ball.move()
  green_ball.move()
  purple_ball.move()
  pink_ball.move()
  window.update()
  time.sleep(0.01)

window.mainloop()