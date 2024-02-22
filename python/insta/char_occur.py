def bit_count(n):
    bit_count = 0

    while n > 0:
        n, rem = divmod(n, 2)
        if rem == 1:
            bit_count += 1

    return bit_count
