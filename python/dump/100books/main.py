import json

def savefile_json(filename, lines):
    try:
        with open(filename, 'w') as file:
            json.dump(lines, file, indent=4)
            return True
    except Exception as e:
        print(e)
        return False
def read_json(filename):
    with open(filename) as file:
        data = json.load(file)
        return data
        

def readlines(filename):
    with open(filename) as file:
        return [line.strip() for line in file.readlines() if line]


def clear_lines(lines:list[str]):
    books = []
    start = 0

    for index in range(7, len(lines), 7):
        data = lines[start: index]
        book = {}
        book["number"] = int(data[0])
        book["name"] = data[1].split("\t")[0]
        book["author"] = data[2].replace("by", "")
        book["rating"] = float(data[3].split()[0])
        book["ratings"] = int(data[3].split("—")[-1].split()[0].replace(',', ''))
        book["f_ratings"] = data[3].split("—")[-1].split()[0]
        books.append(book)
        start = index

    return books

def sorted_by_rating(books):
    books_by_rate = sorted(books, key=lambda book: book.get("rating"), reverse=True)
    return sorted(books_by_rate, key=lambda book: book.get("ratings"), reverse=True)

# data analysis
def rate_gt_4(books):
    res_books = []
    for book in books:
        if book.get("rating") >= 4:
            res_books.append(book)

    # sort by rating
    return sorted(res_books, key=lambda book: book.get("rating"), reverse=True)


def main():
    lines = readlines("books.txt")
    books = clear_lines(lines)
    # savefile_json("books.json", books)
    # sorted_books = sorted_by_rating(books)
    sorted_books = rate_gt_4(books)
    for book in sorted_books[:10]:
        print(book.get("number"),book.get("name"), book.get("rating"), book.get("f_ratings"))


if __name__ == "__main__":
    main()
