def convert_line(c):
    chars = {
        "A": 14,
        "B": 15,
        "C": 16,
        "D": 17,
        "E": 18,
        "F": 19,
        "G": 20,
        "H": 21,
        "I": 22,
        "J": 23,
        "K": 24,
        "L": 25,
        "M": 26,
        "N": 27,
        "O": 28,
    }
    return chars[c] - chars['A']
