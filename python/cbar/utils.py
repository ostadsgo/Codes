""" Simple and small function to be used in the project."""
import re
from itertools import pairwise


def readfile(filename):
    """Get filename and return it's content."""
    content = ""
    try:
        with open(filename, "r", encoding="utf-8") as text_file:
            content = text_file.read()
    except FileNotFoundError as err:
        print(f"{filename} doesn't exsist.", err)
    return content


def element_pattern(text: str) -> list[str]:
    """get elements by pattern."""
    pattern = r"ELEMENT-ID\s*=\s*\d+"
    matches = re.findall(pattern, text)
    return matches


def element_pair(elements: list[str]) -> list[tuple[str]]:
    """Make pair from elements. Each pair is start and end point of a cbar table."""
    return list(pairwise(elements))


def cbar_table(text, pairs):
    """Get a nastran file and extract data between an element pair."""
    # extract only first element!!! change this if you wnat get all elements table
    pair0 = pairs[0]
    start, end = pair0
    pattern = f"{start}(.*?){end}"
    match_result = re.search(pattern, text, flags=re.DOTALL)
    table = {}
    if match_result:
        data = match_result.group(1).split("\n")
        header = [title.strip() for title in data[3].split()]
        sub_header = [title.strip() for title in data[4].split()]
        body = [[float(cell) for cell in row.split()] for row in data[5:-4]]
        table["element_id"] = start
        table["header"] = header
        table["sub_header"] = sub_header
        table["body"] = body

    return table


def get_table(filename):
    """Get a filename and return table repr of the text file"""
    text = readfile(filename)
    matches = element_pattern(text)
    pairs = element_pair(matches)
    table = cbar_table(text, pairs)
    return table


if __name__ == "__main__":
    text = readfile("fileaa")
    matches = element_pattern(text)
    pairs = element_pair(matches)
    table = cbar_table(text, pairs)
    print(table)
