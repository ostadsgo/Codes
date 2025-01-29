# TODO: Calculate area of a rectangle.
# Warning: somthing


try:
    width = int(input("Enter width: "))
    height = int(input("Enter height: "))
    area = width * height
    print("Area is", area)

except ValueError:
    print("Please enter interger value.")


["Even", "Odd"][4 % 2]

["Even", "Odd"][0]


x = ["Even", "Odd"]

x = [4 % 2]

x[0]  # => Even


def hello(name):
    return "hello " + name


hello("John")

import random
