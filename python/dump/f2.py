def f1():
    a = 5
    print(a)


def f2(b):
    b += 2
    print(b)


def f3(i):
    return i * 2


def f4(i):
    return i * 3

a = 1
f1()
b = a
print(b)
f2(b)
c = f3(b)
d = f4(c + 1)
print(c)
print(d)
