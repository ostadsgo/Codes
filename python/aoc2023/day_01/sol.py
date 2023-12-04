import re


def read_input(filename):
    with open(filename) as file:
        lines = file.read().strip().split("\n")
    return lines


def part_one():
    first = 0
    last = 0
    total = 0
    lines = read_input("inputs.txt")
    for line in lines:
        data = re.findall(r"\d", line)
        first, last = data[0], data[-1]
        number = int(first + last)
        total += int(number)

    return total


def pars_int(letters: list) -> list[int]:
    letters_map = {
        # 3 char number letter
        "one": 1,
        "two": 2,
        "six": 6,
        # 4 char numbers
        "four": 4,
        "five": 5,
        "nine": 9,
        # 5 char numbers
        "three": 3,
        "seven": 7,
        "eight": 8,
        "1": 1,
        "2": 2,
        "6": 6,
        "4": 4,
        "5": 5,
        "9": 9,
        "3": 3,
        "7": 7,
        "8": 8,
    }

    for index, letter in enumerate(letters[:]):
        value = letters_map.get(letter)
        if value is not None:
            letters[index] = int(value)

    return letters


def is_number(letter):
    if letter in [
        "one",
        "two",
        "six",
        "four",
        "five",
        "nine",
        "three",
        "seven",
        "eight",
    ]:
        return letter


def get_letter(s, ch, index):
    letter = ""
    if ch in "ots":
        letter = s[index : index + 3]
        if is_number(letter):
            return letter, 3

    if ch in "fn":
        letter = s[index : index + 4]
        if is_number(letter):
            return letter, 4

    if ch in "tse":
        letter = s[index : index + 5]
        if is_number(letter):
            return letter, 5
    return (), 1


def part_two(s):
    data = []
    i = 0
    while i < len(s):
        ch = s[i]
        if ch.isdigit():
            data.append(ch)

        number, inc = get_letter(s, ch, i)
        if number:
            data.append(number)

        i += inc

    numbers = pars_int(data)
    print(s, "-->", numbers)
    return numbers


def part_two_regex(text):
    number_words = re.findall(
        r"\d|(?:one|two|three|four|five|six|seven|eight|nine)",
        text,
        flags=re.IGNORECASE,
    )
    numbers = pars_int(number_words)
    print(text, numbers)
    return numbers


def main():
    total = 0
    lines = read_input("sample_input.txt")
    for line in lines:
        numbers = part_two_regex(line)
        first, last = numbers[0], numbers[-1]
        merged_num = str(first) + str(last)
        total += int(merged_num)
    return total


if __name__ == "__main__":
    result = main()
    print(result)
