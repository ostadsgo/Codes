# Read book and display them.

from file import read_file


books = read_file("books.txt")
print("Index of books: ")

for index, book in enumerate(books):
    print(f"{index} - {book}")
