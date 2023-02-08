def area(width, height):
    if width <= 0 or height <= 0:
        raise ValueError("Width or height must be greather than zero.")
    return width * height


assert area(2, 3) == 6
assert area(7, 2) == 14
assert area(6, 3) == 18

