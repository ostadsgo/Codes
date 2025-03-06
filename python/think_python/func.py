from turtle import left, right, forward, done
import math


def square(length):
    for i in range(4):
        forward(length)
        left(90)


def polyline(n, length, angle):
    for i in range(n):
        forward(length)
        left(angle)


def polygon(n, length):
    angle = 360 / n
    polyline(n, length, angle)


def arc(radius, angle):
    arc_length = 2 * math.pi * radius * angle / 360
    n = 30
    length = arc_length / n
    step_angle = angle / n
    polyline(n, length, step_angle)


def circle(radius):
    arc(radius, 360)


def parallelogram(width, height, angle):
    for i in range(4):
        forward([height, width][i % 2])
        left(180 - angle)


def rectangle(width, height):
    parallelogram(width, height, 90)


# this is not working
def rhombus(length, angle):
    parallelogram(length, length, angle)


# rectangle(40, 60)
rhombus(40, 60)

done()
