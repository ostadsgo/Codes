from math import sqrt



def normal():
    chars = "aaaabbaaccaadddcaad"
    counter = {}
    for char in chars:
        if char in counter:
            counter[char] = counter[char] + 1
        else:
            counter[char] = 1

    print(counter)  # {'a': 10, 'b': 2, 'c': 3, 'd': 4}


chars = "aaaabbaaccaadddcaad"
counter = {}
for char in chars:
    counter[char] = counter.setdefault(char, 0) + 1

print(counter)
