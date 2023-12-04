# day 02 of Advent of code 2023
# Saeed Gholami (ostadsgo)


from typing_extensions import is_protocol


def read_input(filename):
    with open(filename) as file:
        lines = file.readlines()
    return lines


letters = {
    # 3 char number letter
    "1",
    "2",
    "6",
    # 4 char number letter
    "4",
    "5",
    "9",
    # 5 char number letter
    "3",
    "7",
    "8",
}

letters_map = {
    # 3 char number letter
    "one": "1",
    "two": "2",
    "six": "6",
    # 4 char number letter
    "four": "4",
    "five": "5",
    "nine": "9",
    # 5 char number letter
    "three": "3",
    "seven": "7",
    "eight": "8",
}

def is_number_letter(letter, letter_len=3):
    one_two_six = list(letters_map.keys())[:3]
    four_five_nine = list(letters_map.keys())[3:6]
    three_seven_eight = list(letters_map.keys())[6:]
    if letter_len == 3:
        if letter in one_two_six:
            return True
    if letter_len == 4:
        if letter in four_five_nine:
            pass
    if letter_len == 5:
        if letter in three_seven_eight:
            pass



extracted_letters = []
s = "oneeightwothree"
start = 0

while True:
    for inc in [3, 4, 5]:
        letter = s[start: start + inc]
        if is_number_letter(letter, inc):
            extracted_letters.append(letter)
            start = start + inc
        


print(extracted_letters)

# 0:3
# 0:4
# 0:5
# 5:8
# 8:12
# 12:17
#
