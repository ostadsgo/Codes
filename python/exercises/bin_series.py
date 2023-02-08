def binary_validate(s):
    first_byte = s[:8]
    second_byte = s[8:16]
    third_byte = s[16:]
    print(int(first_byte, 2), -int(second_byte[1:], 2), chr(int(third_byte, 2)))


binary_validate("111100011110110100100100")
# # Tests
# assert binary_validate("111100011110110100100100") == [241, -109, "$"]
# assert binary_validate("010000110111110001110000") == [67, 124, "p"]
# assert binary_validate("101110101011") == "Error"
# assert binary_validate("010111900010111001011010") == "Error"
# assert binary_validate("0101p0001010417001001m01") == "Error"
