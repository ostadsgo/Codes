for i in range(10):
    print('*' * i)


j = 1
for i in range(10, 0, -1):
    print((j * ' ') + (i * '*'))
    j += 1
