from os import listdir
books = listdir("./Books")
print(len(books))
with open("books.txt", "w", encoding="utf-8") as file:
    for book in books:
        file.write(book + '\n')
