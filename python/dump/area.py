# Calculate area of a rectangle.

try:
    width = int(input("Enter width: "))
    height = int(input("Enter height: "))
    area = width * height
    print("Area is", area)
except ValueError:
    print("Please enter interger value.")

