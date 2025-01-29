import tkinter as tk
from time import sleep

WIDTH = 800
HEIGHT = 600

root = tk.Tk()
root.title("Animation")
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

ball = canvas.create_oval(10, 10, 60, 60, fill="orange")
xspeed = 4
yspeed = 5
while True:
    canvas.move(ball, xspeed, yspeed)
    pos = canvas.coords(ball)
    if pos[3] > HEIGHT or pos[1] <= 0:
        yspeed = -yspeed
    if pos[2] > WIDTH or pos[0] <= 0:
        xspeed = -xspeed
    
    canvas.update()
    sleep(.01)

root.mainloop()
