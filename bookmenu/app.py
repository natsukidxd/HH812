from bookapi import *
from os import system

WIDTH: int = 120
HEIGHT: int = 30

def addbook() -> bool:
    system("cls")
    print(" " * int((WIDTH - 13)/ 2))
    isbn: str "ISBN       : "
    "TITLE      : "
    "COPYRIGHT  : "
    "AUTHOR     : "
    "PRICE      : "
    "QTY        : "


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
            input("Press Enter to continue...".center(WIDTH, " "))
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
            input("Press Enter to continue...".center(WIDTH, " "))


if __name__ == "__main__":
    main()
