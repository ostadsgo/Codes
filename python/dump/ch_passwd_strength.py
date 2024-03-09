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

def has_upper(passwd: str) -> bool:
    for ch in passwd:
        if ch.isupper:
            return True
    return False

def has_punch(passwd: str) -> bool:
    for ch in passwd:
        if ch in punctuation:
            return True
    return False

def has_num(passwd: str) -> bool:
    for ch in passwd:
        if ch in  "1234567890":
            return True
    return False

def is_it_strong(passwd: str) -> bool:
    """ If the length of the passwd is 8 character or more 
        and it is contain at least one upper char one puncuation 
        and one number return True otherwise False
    """
    conds = [
        len(passwd) >= 8,
        has_upper(passwd),
        has_punch(passwd),
        has_num(passwd)
    ]


assert password_strength("Python!") == 2
print("✅ Test #1 passed")
assert password_strength("Python") == 1
print("✅ Test #2 passed")
assert password_strength("python") == 0
print("✅ Test #3 passed")



