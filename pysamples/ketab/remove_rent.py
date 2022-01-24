# Get index of the book from rented list and delete them from rents.txt
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

books = read_file("books.txt")

print("Rented books count:", len(rented_books))
for index, book in enumerate(rented_books):
    print("{} - {} Rented by: {}".format(index, book, rents_dict[book]))

book_index = int(input("Enter book id for remove rent: "))
if book_index in range(len(rented_books)):
    # get the name of the book to remove from rents_dict
    book = rented_books[book_index]
    del rents_dict[book]  # delete the book using its name which is out key in dict
    # write after delete the rented book
    write_file_dict("rents.txt", rents_dict)
else:
    print("Error! Book index not found.")
