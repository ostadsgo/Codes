def f(i, values=[]):
    values.append(i)
    print(values, "id of values", hex(id(values)))
    return values


f(1)
f(2)
f(3)

