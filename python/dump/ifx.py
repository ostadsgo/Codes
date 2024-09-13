import time


def ifx(expr, a, b):
    if expr:
        return a
    return b


start = time.time()
for i in range(1000_000_0):
    a = 5
    b = 9
    max_val = ifx(a > b, a, b)
end = time.time()

print(f"Time is {end - start} second")

##start = time.time()
##for i in range(1000_000_0):
##    a = 5
##    b = 9
##            
##    max_val2 = a if a > b else b
##end = time.time()
##print(f"Time is {end - start} second")




