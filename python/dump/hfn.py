def is_even(x):
    return x % 2 == 0


def all_evens(numbers: list[int]) -> list[int]:
    """ Get list of numbers and return the even numbers as a list. """
    evens = []
    for num in numbers:
        if num % 2 == 0:
            evens.append(num)
    return evens

def all_evens(numbers):
    return list(filter(is_even, numbers))

def all_evens(numbers):
    return list(filter(lambda n: n % 2 == 0, numbers))


def test_all_evens():
    numbers = [3, 9, 1, 2, 4, 33, 23, 12, 9, 3]
    numbers2 = [1, 1, 1, 1]
    numbers3 = []
    print("Start testing....")
    assert all_evens(numbers) == [2, 4, 12]
    print("✅ Test 1 passed.")
    assert all_evens(numbers2) == []
    print("✅ Test 2 passed.")
    assert all_evens(numbers3) == []
    print("✅ Test 3 passed.")
    print("All tests passed successfuly.")


test_all_evens()









