# User select a book index to rent.
# All rented books stored in rents.txt with the format of `book name, customer name`

from file import read_file, write_file_dict


rents = read_file("rents.txt")

# list of rented books.
rented_books = []
# will be used to saved all books,renter name including new rent record.
rents_dict = {}
for rent in rents:
    book, customer = rent.split(",")
    rented_books.append(book)
    rents_dict[book] = customer

# # get all books form the books.txt file
books = read_file("books.txt")
print(f"Book Number: {len(books)} | Rented Count: {len(rented_books)}")

# Print book status (book rented by who or book availabity)
for i, book in enumerate(books):
    msg = f"{i} - {book} : "  # This msg plus rented person name or available sring.
    if book in rented_books:
        msg += rents_dict[book]  # rents_dict used to figuare out customer name
    else:
        msg += "Available"
    print(msg)

# Add rent section.
book_index = int(input("Enter book id for rent: "))
if book_index >= 0 and book_index < len(books):
    book = books[book_index]
    if book in rented_books:  # check if book rented or not.
        print(f"{book}' is rented by {rents_dict[book]} previously.")
    else:
        name = input("Enter the name of renter: ")
        rents_dict[book] = name
        write_file_dict("rents.txt", rents_dict)
        print(f"Done.")
else:
    print("Error! Book index not found.")
