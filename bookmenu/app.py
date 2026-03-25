from bookapi import *
from os import system

WIDTH: int = 120
HEIGHT: int = 30


def addbook() -> None:

    titlemenu("add book")
    isbn: str = ""
    title: str = ""
    copyright: str = ""
    author: str = ""
    price: float = 0
    qty: int = 0
    try:
        print(end=" " * int((WIDTH - 13) / 2))
        isbn = input("ISBN       : ")
        print(end=" " * int((WIDTH - 13) / 2))
        title = input("TITLE      : ")
        print(end=" " * int((WIDTH - 13) / 2))
        copyright = input("COPYRIGHT  : ")
        print(end=" " * int((WIDTH - 13) / 2))
        author = input("AUTHOR     : ")
        print(end=" " * int((WIDTH - 13) / 2))
        price = float(input("PRICE      : "))
        print(end=" " * int((WIDTH - 13) / 2))
        qty = int(input("QTY        : "))
        print(end=" " * int((WIDTH - 13) / 2))
        print(f"TOTAL      : {float(price * qty):.2f}")
    except Exception as err:
        errormessage: str = f"Error: {err}"
        print(end=" " * int((WIDTH - len(errormessage)) / 2))
        print(errormessage)
        return

    add_book(isbn, title, copyright, author, str(price), str(qty))


def findbook() -> None:

    titlemenu("find book")
    print(end=" " * int((WIDTH - 13) / 2))
    isbn: str = input("ISBN       : ")
    book_data: list = find_book(isbn)
    if book_data != []:
        print(end=" " * int((WIDTH - 13) / 2))
        print(f"TITLE      : {book_data[1]}")
        print(end=" " * int((WIDTH - 13) / 2))
        print(f"COPYRIGHT  : {book_data[2]}")
        print(end=" " * int((WIDTH - 13) / 2))
        print(f"AUTHOR     : {book_data[3]}")
        print(end=" " * int((WIDTH - 13) / 2))
        print(f"PRICE      : {book_data[4]}")
        print(end=" " * int((WIDTH - 13) / 2))
        print(f"QTY        : {book_data[5]}")
        print(end=" " * int((WIDTH - 13) / 2))
        print(f"TOTAL      : {float(float(book_data[4]) * int(book_data[5])):.2f}")
    else:
        print("No book found".center(WIDTH, " "))


def editbook() -> None:
    titlemenu("edit book")
    isbn: str = ""
    title: str = ""
    copyright: str = ""
    author: str = ""
    price: float = 0
    qty: int = 0
    try:
        print(end=" " * int((WIDTH - 13) / 2))
        isbn = input("ISBN       : ")
        print(end=" " * int((WIDTH - 13) / 2))
        title = input("TITLE      : ")
        print(end=" " * int((WIDTH - 13) / 2))
        copyright = input("COPYRIGHT  : ")
        print(end=" " * int((WIDTH - 13) / 2))
        author = input("AUTHOR     : ")
        print(end=" " * int((WIDTH - 13) / 2))
        price = float(input("PRICE      : "))
        print(end=" " * int((WIDTH - 13) / 2))
        qty = int(input("QTY        : "))
        print(end=" " * int((WIDTH - 13) / 2))
        print(f"TOTAL      : {float(price * qty):.2f}")
    except Exception as err:
        errormessage: str = f"Error: {err}"
        print(end=" " * int((WIDTH - len(errormessage)) / 2))
        print(errormessage)
        return
    
    isokay:bool = update_book(isbn, title, copyright, author, str(price), str(qty))

    if isokay: print("Book updated.".center(WIDTH, " "))
    else: print("Book not found".center(WIDTH, " "))

def titlemenu(titletext: str) -> None:
    system("cls")
    print(f"{titletext.upper()}".center(WIDTH, "-"))


def displaymenu() -> None:
    system("cls")
    menuitems: list = [
        "1. ADD BOOK         ",
        "2. FIND BOOK        ",
        "3. EDIT BOOK        ",
        "4. DELETE BOOK      ",
        "5. DISPLAY ALL BOOK ",
        "0. QUIT/END         ",
    ]

    for _ in range(0, 15 - len(menuitems)):
        print()

    print("-" * WIDTH)
    print("MENU".center(WIDTH, " "))
    print("-" * WIDTH)
    [print(menuitems[i].center(WIDTH, " ")) for i in range(0, len(menuitems))]


def main() -> None:
    option: int = 9999
    while option != 0:
        displaymenu()
        print("-" * WIDTH)

        optionmessage: str = "ENTER OPTION(0..5): "
        print(end=" " * int((WIDTH - len(optionmessage)) / 2))

        raw = input(optionmessage)
        if not raw.isdigit():
            print("INVALID OPTION".center(WIDTH, " "))
            continuemessage: str = "Press Enter to continue..."
            print(end=" " * int((WIDTH - len(continuemessage)) / 2))
            input(continuemessage)
            continue

        option = int(raw)

        if option == 1:
            addbook()
        elif option == 2:
            findbook()
        elif option == 3:
            editbook()
        elif option == 4:
            deletebook()
        elif option == 5:
            displayallbook()
        elif option == 0:
            print("PROGRAM ENDED".center(WIDTH))
        else:
            print("INVALID OPTION".center(WIDTH, " "))
        if option != 0:
            continuemessage: str = "Press Enter to continue..."
            print(end=" " * int((WIDTH - len(continuemessage)) / 2))
            input(continuemessage)


if __name__ == "__main__":
    main()
