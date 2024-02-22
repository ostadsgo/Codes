import time
import timeit
from math import factorial


def fact_for(n=10_000):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


def fact_rec(n):
    if n <= 1:
        return 1
    return n * fact_rec(n - 1)


## Using timit modlue to get time execution of a block of code.
res = timeit.timeit(lambda x: factorial(10), number=100)
print(res)

## First way of getting time execution.
# time execution.
# start = time.time()
# # fact_for(100_000)  # 4.093
# factorial(100_000)
# end = time.time()
# duration = round(end - start, 3)
# print(duration, "seconds")

# Tests
# assert fact_for(-1) == 1
# print("Test 1 passed.")
# assert fact_for(0) == 1
# print("Test 2 passed.")
# assert fact_for(1) == 1
# print("Test 3 passed.")
# assert fact_for(5) == 120
# print("Test 4 passed.")
#
# # tests fact_rec
# assert fact_rec(-1) == 1
# print("Test 1 passed.")
# assert fact_rec(0) == 1
# print("Test 2 passed.")
# assert fact_rec(1) == 1
# print("Test 3 passed.")
# assert fact_rec(5) == 120
# print("Test 4 passed.")
