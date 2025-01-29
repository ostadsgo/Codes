import math


# x = math.gcd(12, 6)
# print(x)
def gcd(a, b):
    if a % b <= 0:
        return b
    else:
        return gcd(b % (a % b), (a % b))



a = 180
b = 12

while a % b > 0:
    r = a % b
    a = b
    b = r



print(b)

