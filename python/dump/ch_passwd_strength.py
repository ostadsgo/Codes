# password = "Pyth0n&me"
# symobls = "!@#$%%^&*()_+-="
# is_upper = 0
# is_digit = 0 
# is_symbol = 0
# pass_length = 8
# for ch in password:
#     if ch.isupper():
#         is_upper += 1
#     if ch.isdigit():
#         is_digit += 1
#     if ch in symobls:
#         is_symbol += 1
#     print(ch, "is upper", is_upper, "is digit", is_digit, "is symbol", is_symbol)
#
# strength = is_upper + is_digit + is_symbol
# print(strength)
#
#
from string import punctuation


def password_strength(password: str) -> int:
    strength = 0
    for ch in password:
        if ch.isupper():
            strength += 1
        if ch.isdigit():
            strength += 1
        if ch in punctuation:
            strength += 1
    return strength

def password_strength(password: str) -> int:
    strength = 0
    for ch in password:
        rules = [ch.isupper(), ch.isdigit(), ch in punctuation]
        strength += 1 if any(rules) else 0
    return strength


assert password_strength("Python!") == 2
print("✅ Test #1 passed")
assert password_strength("Python") == 1
print("✅ Test #2 passed")
assert password_strength("python") == 0
print("✅ Test #3 passed")



