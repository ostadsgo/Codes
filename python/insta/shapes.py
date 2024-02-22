def square(a: int, shape: str):
    space_num = a * 2 - 4
    side = shape + " " * space_num + shape + "\n"
    print(shape * a)
    print(side * (a - 2), end="")
    print(shape * a)


for i in range(5, 20, 5):
    square(i, "* ")
