import tkinter as tk
from time import sleep
from random import randrange, choice

WIDTH = 800
HEIGHT = 600

root = tk.Tk()
root.title("Animation")
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

class Ball:
    def __init__(self, color, size):
        self.shape = canvas.create_oval(10, 10, size, size, fill=color)
        self.xspeed = randrange(1, 100)
        self.yspeed = randrange(1, 100)

    def move(self):
        canvas.move(self.shape, self.xspeed, self.yspeed)
        pos = canvas.coords(self.shape)
        if pos[3] > HEIGHT or pos[1] <= 0:
            self.yspeed = -self.yspeed
        if pos[2] > WIDTH or pos[0] <= 0:
            self.xspeed = -self.xspeed


# Make some balls
balls = []
for i in range(1000):
    color = choice(["red", "green", "blue", "yellow", "black", "brown", "orange"])
    size = randrange(5, 25)
    ball = Ball(color, size)
    balls.append(ball)


while True:
    for ball in balls:
        ball.move()
    canvas.update()
    sleep(.01)

root.mainloop()
