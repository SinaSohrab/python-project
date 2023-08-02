book = {}

while True:
    print("add book [1]")
    print("remove book [2]")
    print("edit book [3]")
    print("show book [4]")
    number = int(input("Choose one of the options: "))

    if number == 1:
        value = input("Enter the name book: ")
        key = input("Enter the book's subject: ")
        book[value] = key

    if number == 2:
        name_book = input("remove book :")
        del book[name_book]

    if number == 3:
        name_book = input("The name of the book you want to change: ")
        del book[name_book]
        value_new_book = input("The new name of the book: ")
        key_new_book = input("New topic of the book: ")
        book[value_new_book] = key_new_book

    if number == 4:
        print(book)
