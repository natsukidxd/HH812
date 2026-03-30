"""
Student List
"""

from os import system

CONSOLE_WIDTH: int = 120
CONSOLE_HEIGHT: int = 30
NOT_FOUND: int = -1

students: list = [
    {
        "idno": "1000",
        "lastname": "golf",
        "firstname": "lima",
        "course": "bsit",
        "level": "3",
    },
    {
        "idno": "2000",
        "lastname": "uniform",
        "firstname": "quebec",
        "course": "bscs",
        "level": "3",
    },
    {
        "idno": "4000",
        "lastname": "india",
        "firstname": "papa",
        "course": "bsit",
        "level": "2",
    },
    {
        "idno": "5000",
        "lastname": "oscar",
        "firstname": "sierra",
        "course": "bsit",
        "level": "1",
    },
]


def title(titletext: str) -> None:
    system("cls")
    print(f"{titletext.upper()}".center(CONSOLE_WIDTH, "-"))


def displaylist() -> None:
    title("student list")

    if not students:
        print("NO STUDENTS FOUND".center(CONSOLE_WIDTH, " "))
        print("NOTHING FOLLOWS".center(CONSOLE_WIDTH, "-"))
        return

    header: list = list(students[0].keys())
    for head in header:
        print(f"{head.upper():<20}", end="")
    print()
    print("-" * CONSOLE_WIDTH)

    for student in students:
        values: list = list(student.values())
        for val in values:
            print(f"{str(val).upper():<20}", end="")
        print()

    print("NOTHING FOLLOWS".center(CONSOLE_WIDTH, "-"))


def addstudent() -> None:
    title("add student")

    print(end=" " * 50)
    idno: str = input("IDNO      : ")
    print(end=" " * 50)
    lastname: str = input("LASTNAME  : ")
    print(end=" " * 50)
    firstname: str = input("FIRSTNAME : ")
    print(end=" " * 50)
    course: str = input("COURSE    : ")
    print(end=" " * 50)
    level: str = input("LEVEL     : ")

    if idno and lastname and firstname and course and level:
        for student in students:
            if student["idno"] == idno:
                print()
                print("IDNO ALREADY EXISTS".center(CONSOLE_WIDTH, " "))
                return

        student: dict = {
            "idno": idno,
            "lastname": lastname,
            "firstname": firstname,
            "course": course,
            "level": level,
        }
        students.append(student)
        print()
        print("NEW STUDENT ADDED".center(CONSOLE_WIDTH, " "))
    else:
        print()
        print("FILL ALL FIELDS".center(CONSOLE_WIDTH, " "))


def findstudent(show_result: bool = True) -> int:
    title("find student")

    print(end=" " * 50)
    idno: str = input("Enter IDNO: ")

    index = NOT_FOUND
    for i, student in enumerate(students):
        if student["idno"] == idno:
            index = i
            break

    if index != NOT_FOUND:
        if show_result:
            title("student found")
            print()
            print("-" * CONSOLE_WIDTH)

            header: list = list(students[0].keys())
            for head in header:
                print(f"{head.upper():<20}", end="")
            print()
            print("-" * CONSOLE_WIDTH)

            values: list = list(students[index].values())
            for val in values:
                print(f"{str(val).upper():<20}", end="")
            print()
            print("NOTHING FOLLOWS".center(CONSOLE_WIDTH, "-"))
        return index
    else:
        print()
        print("STUDENT NOT FOUND".center(CONSOLE_WIDTH, " "))
        return NOT_FOUND


def deletestudent() -> None:
    index = findstudent()

    if index == NOT_FOUND:
        return

    message: str = "Are you sure you want to delete? Y/N : "
    print()
    print(end=" " * int((CONSOLE_WIDTH - len(message)) / 2))
    option: str = input(message)

    if option.upper() == "Y":
        students.pop(index)
        print("STUDENT DELETED".center(CONSOLE_WIDTH, " "))
    else:
        print("STUDENT NOT DELETED".center(CONSOLE_WIDTH, " "))


def displaymenu() -> None:
    system("cls")
    menuitems: list = [
        "1. DISPLAY ALL STUDENT ",
        "2. FIND STUDENT        ",
        "3. ADD STUDENT         ",
        "4. DELETE STUDENT      ",
        "5. UPDATE STUDENT      ",
        "0. QUIT/END            ",
    ]

    for _ in range(0, 15 - len(menuitems)):
        print()

    print("=" * CONSOLE_WIDTH)
    print("MENU".center(CONSOLE_WIDTH, " "))
    print("=" * CONSOLE_WIDTH)
    print()

    for item in menuitems:
        print(item.center(CONSOLE_WIDTH, " "))


def updatestudent() -> None:
    index = findstudent()

    if index == NOT_FOUND:
        return

    print()
    print("UPDATING STUDENT".center(CONSOLE_WIDTH, " "))

    print(end=" " * 50)
    idno: str = input("IDNO      : ")
    print(end=" " * 50)
    lastname: str = input("LASTNAME  : ")
    print(end=" " * 50)
    firstname: str = input("FIRSTNAME : ")
    print(end=" " * 50)
    course: str = input("COURSE    : ")
    print(end=" " * 50)
    level: str = input("LEVEL     : ")

    if idno and lastname and firstname and course and level:
        for student in students:
            if student["idno"] == idno:
                print()
                print("IDNO ALREADY EXISTS".center(CONSOLE_WIDTH, " "))
                return
        student: dict = {
            "idno": idno,
            "lastname": lastname,
            "firstname": firstname,
            "course": course,
            "level": level,
        }
        students[index] = student
        print("STUDENT UPDATED!".center(CONSOLE_WIDTH, " "))
    else:
        print("STUDENT NOT UPDATED!".center(CONSOLE_WIDTH, " "))


def main() -> None:
    option: int = 9999

    while option != 0:
        displaymenu()
        print(end=" " * 50)

        raw = input("Enter Option(0..5): ")
        if not raw.isdigit():
            print("INVALID OPTION".center(CONSOLE_WIDTH, " "))
            input("Press Enter to continue...".center(CONSOLE_WIDTH, " "))
            continue

        option = int(raw)

        if option == 1:
            displaylist()
        elif option == 2:
            findstudent()
        elif option == 3:
            addstudent()
        elif option == 4:
            deletestudent()
        elif option == 5:
            updatestudent()
        elif option == 0:
            print("PROGRAM ENDED".center(CONSOLE_WIDTH))
        else:
            print("INVALID OPTION".center(CONSOLE_WIDTH, " "))
        if option != 0:
            input("Press Enter to continue...".center(CONSOLE_WIDTH, " "))


if __name__ == "__main__":
    main()
