# read all book from books.txt file
def read_file(filename):
    file = open(filename)
    books = [line.strip() for line in file.readlines()]
    file.close()
    return books


# write all books to books.txt file
def write_file(filename, data):
    file = open(filename, "w")
    for item in data:
        file.write(item + "\n")
    file.close()


def write_file_dict(filename, data):
    file = open(filename, "w")
    for key, value in data.items():
        file.write(f"{key},{value}\n")
    file.close()
