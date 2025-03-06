def sword(s):
    res = []
    for word in s.split():
        if len(word) > 5:
            res.append(word[::-1])
        else:
            res.append(word)
    return " ".join(res)

def sword(s):
    print( " ".join(word[::-1] if len(word) >= 5 else word for word in s.split()))

assert sword("Hey fellow warriors") == "Hey wollef sroirraw"
assert sword("This sentence is a sentence") == "This ecnetnes is a ecnetnes"
