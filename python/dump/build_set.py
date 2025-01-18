# what is the set?
# set is python list but unique items 
# so we need to make a list unique and we will got a set
# the function `set` make a list unique

def myset(items):
    u = []
    for item in items:
        if item not in u:
            u.append(item)

    return u


assert myset([1, 1, 1, 2, 3, 4]) == [1, 2, 3, 4]


# What is the union?
# it is two list combined together and uniqufied
def my_union(a, b):
    ab = []
    for item in a:
        ab.append(item)
    for item in b:
        ab.append(item)

    return myset(ab)

assert my_union([1, 1, 2, 3], [3, 3, 4, 5]) == [1, 2, 3, 4, 5]


def my_intersection(a, b):
    a = myset(a)
    b = myset(b)
    intersection = []
    for item in a:
        if item in b:
            intersection.append(item)

    return intersection


assert my_intersection([1, 1, 2, 3], [1, 2, 4]) == [1, 2]


def my_diff(a, b):
    a = myset(a)
    b = myset(b)
    diff = []
    for item in a:
        if item not in b:
            diff.append(item)
    return diff

assert my_diff([1, 1, 2, 3], [1, 2, 4]) == [3]


