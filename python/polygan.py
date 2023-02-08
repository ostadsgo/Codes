# polygan.py
# draw regualr polygans

from turtle import *



def polygan(n, length):
    for _ in range(n):
        forward(length)
        left(360 / n)

def main():
    for n in range(3, 10):
        polygan(n, 80)

main()
