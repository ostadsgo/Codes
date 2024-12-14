import timeit


def sum_1(*numbers):
    return sum(numbers)


def sum_2(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total


t1 = timeit.timeit(lambda: sum_1(*range(1, 1000)), number=10_000)
t2 = timeit.timeit(lambda: sum_2(*range(1, 1000)), number=10_000)

print(f"{t1:.2f}", "Seconds")
print(f"{t2:.2f}", "Seconds")
