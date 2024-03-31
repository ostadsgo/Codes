# 4.1.1 Counting
def count(element, lst):
    c = 0
    for elm in lst:
        if elm == element:
            c += 1
    return c


# 4.1.2 Support Contains
def support_contains(needed, support):
    for letter in needed:
        if count(letter, needed) > count(letter, support):
            return False
    return True

