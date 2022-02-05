from file import read_books, write_books


def display_list_of_books(books):
    for index, book in enumerate(books):
        print(f"{index} - {book}")


# Display all indexes and books name.
print("Index of books: ")
books = read_books()
display_list_of_books(books)

# Get index of the book to delete it.
book_index = int(input("Enter index of book for remove or -1 to exit: "))

while book_index != -1:
    if book_index >= 0 and book_index < len(books):  # validate book index (book id)
        books.remove(books[book_index])  # delete book from books list
        print("Book deleted from list.")
        write_books(books)  # write book to the file.
        print("New books updated in our DB.")
    else:  # if index not found this message will print out.
        print(f"Index {book_index} not found in our DB.")

    print("Index of books: ")
    display_list_of_books(books)
    book_index = int(input("Enter index of book for remove or -1 to exit: "))
