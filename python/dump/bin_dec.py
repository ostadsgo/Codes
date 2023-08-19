def binary_to_decimal(number):
    i = 0
    res = 0
    while number > 0:
        digit = number % 10
        number = number // 10
        res += digit * (2 ** i)
        i += 1
    return res


assert binary_to_decimal(1001) == 9
assert binary_to_decimal(1100) == 12
assert binary_to_decimal(1011) == 11
print("All tests passed successfuly.")

    
    

