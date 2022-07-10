from tkinter import *
import time

def player_1_up(event):
    canvas.move(player_1, 0, -20)

def player_1_down(event):
    canvas.move(player_1, 0, 20)

def player_2_up(event):
    canvas.move(player_2, 0, -20)

def player_2_down(event):
    canvas.move(player_2, 0, 20)

window = Tk()

WIDTH = 750
HEIGHT = 750

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

ball = canvas.create_oval(100, 100, 0, 0, fill="red")
canvas.move(ball, 30, 30)

player_1 = canvas.create_rectangle(0,0,30,150,fill="blue")
player_2 = canvas.create_rectangle(WIDTH-30,0,750,150,fill="green")

window.bind("<w>", player_1_up)
window.bind("<s>", player_1_down)

window.bind("<Up>", player_2_up)
window.bind("<Down>", player_2_down)

yVelocity = 3
xVelocity = 4

while True:
    coordinates = canvas.coords(ball)
    print(coordinates)

    if (coordinates[2] >= (canvas.winfo_width()-30) or coordinates[0]<30):
        xVelocity = -xVelocity
    if (coordinates[3] >= (canvas.winfo_height()) or coordinates[1]<0):
        yVelocity = -yVelocity


    canvas.move(ball, xVelocity, yVelocity)
    window.update()

    time.sleep(0.01)

window.mainloop()