def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    return "Odd"


def even_or_odd(number):
    return ["Even", "Odd"][number % 2]

print(even_or_odd(10))
print(even_or_odd(3))

