a = 5
b = 1
c = 5

if a <= b + c:
    if b <= a + c:
        if c <= a + b:
            print("Can make a triangle")
        else:
            print("Cann't make a triangle")
    else:
        print("Cann't make a triangle")
else:
    print("Cann't make a triangle")
