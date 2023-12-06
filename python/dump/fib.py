# Make a fibonacci series using Python


#0, 1, 1, 2, 3, 5, 8

def fib(n):
    a = 0
    b = 1
    c = 0
    while  b < n:
        c = a + b
        a = b
        b = c
        print(a)

    


def fib2(n):
    a = 0
    b = 1
    i = 0
    total = 0
    while i < n:
        a, b = b, a + b
        print(a, end=" ")
        total += a
        i += 1
    print()
    return total

res = fib2(10)
print("total of the numbers: ", res)






