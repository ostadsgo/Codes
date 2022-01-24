# Insert book
# Get a book name from user and add it to the books.txt file.

from file import read_file, write_file


books = read_file("books.txt")
name = input("Add book name or 'exit': ")

while name != "exit":
    if name in books:
        print("Book is added before. Try another book.")
    else:
        books.append(name)
        print(f"A book with name: '{name}' inserted.")
    name = input("Add book name or 'exit': ")

write_file("books.txt", books)
print("Writing books to disk.")
