def binary_to_decimal(number):
    i = 0
    res = 0
    while number > 0:
        digit = number % 10
        number = number // 10
        res += digit * (2 ** i)
        i += 1
    return res


print(binary_to_decimal(11100))

    
    

