import turtle


joe = turtle.Pen()
joe.color("black")
joe.speed(0)

def square(length=100):
    for i in range(4):
        joe.forward(length)
        joe.left(90)

def circle(radius):
    joe.circle(radius)

def star(length, color):
    joe.color(color)
    for _ in range(8):
        joe.forward(length)
        joe.left(225)

def fractol():
    for i in range(20):
        joe.forward(10 * i)
        joe.left(90)


def circle_fractol():
    for i in range(50):
        joe.circle(2 * i)
        joe.left(10)

def fractol_experment():
    for i in range(100):
        joe.forward(i*2)
        joe.circle(i*2, 90)
        joe.right(20)

fractol_experment()
