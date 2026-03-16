"""
    Student List
"""

from os import system

CONSOLE_WIDTH: int = 120
CONSOLE_HEIGHT: int = 30
NOT_FOUND: int = -1

students: list = [
    {
        'idno': '1000',
        'lastname': 'golf',
        'firstname': 'lima',
        'course': 'bsit',
        'level': '3',
    },
    {
        'idno': '2000',
        'lastname': 'uniform',
        'firstname': 'quebec',
        'course': 'bscs',
        'level': '3',
    },
    {
        'idno': '4000',
        'lastname': 'india',
        'firstname': 'papa',
        'course': 'bsit',
        'level': '2',
    },
    {
        'idno': '5000',
        'lastname': 'oscar',
        'firstname': 'sierra',
        'course': 'bsit',
        'level': '1',
    },
]



def title(titletext: str) -> None:
    system('cls')
    print(f"{titletext.upper()}".center(CONSOLE_WIDTH, '-'))


def displaylist() -> None:
    title('student list')

    if not students:
        print("NO STUDENTS FOUND".center(CONSOLE_WIDTH, ' '))
        print('NOTHING FOLLOWS'.center(CONSOLE_WIDTH, '-'))
        return

    header: list = list(students[0].keys())
    for head in header:
        print(f"{head.upper():<20}", end="")
    print()
    print('-' * CONSOLE_WIDTH)

    for student in students:
        values: list = list(student.values())
        for val in values:
            print(f"{str(val).upper():<20}", end="")
        print()

    print('NOTHING FOLLOWS'.center(CONSOLE_WIDTH, '-'))


def addstudent() -> None:
    title('add student')
    idno:str = input('IDNO      : ')
    lastname:str = input('LASTNAME  : ')
    firstname:str = input('FIRSTNAME : ')
    course:str = input('COURSE    : ')
    level:str = input('LEVEL     : ')

    if idno and lastname and firstname and course and level:
        for student in students:
            if student['idno'] == idno:
                print()
                print('IDNO ALREADY EXISTS'.center(CONSOLE_WIDTH, ' '))
                return

        student: dict = {
            'idno': idno,
            'lastname': lastname,
            'firstname': firstname,
            'course': course,
            'level': level,
        }
        students.append(student)
        print()
        print('NEW STUDENT ADDED'.center(CONSOLE_WIDTH, ' '))
    else:
        print()
        print("FILL ALL FIELDS".center(CONSOLE_WIDTH, ' '))


def findstudent(show_result: bool = True) -> int:
    title('find student')
    idno:str = input("Enter IDNO: ")
    student:dict={}
    for student in students:
        if student['idno'] == idno:
            index = i
            break
    
    if index != 9999:
        header:list = list(students[0].keys())
        [print(f"{head.upper():<20}", end = "") for head in header]
        print()
        print('-' * 120)
        values:list = list(student.values())
        [print(f"{val.upper():<20}", end = "") for val in values]
        print()
        print('Student Found'.center(VERTICAL, ' '))
    else:
        print()
        print('Student Not Found'.center(VERTICAL, ' '))

def deletestudent()->None:
    findstudent()
    students.pop(index)
    print('Student Deleted'.center(VERTICAL, ' '))

def displaymenu() -> None:
    system('cls')
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

    print('=' * CONSOLE_WIDTH)
    print("MENU".center(CONSOLE_WIDTH, " "))
    print('=' * CONSOLE_WIDTH)
    print()

    for item in menuitems:
        print(item.center(CONSOLE_WIDTH, ' '))


def updatestudent() -> None:
    index = findstudent()

    if index == NOT_FOUND:
        return

    print()
    print('UPDATING STUDENT'.center(CONSOLE_WIDTH, ' '))

    print(end =' ' * 50)
    idno:str = input('IDNO      : ')
    print(end =' ' * 50)
    lastname:str = input('LASTNAME  : ')
    print(end =' ' * 50)
    firstname:str = input('FIRSTNAME : ')
    print(end =' ' * 50)
    course:str = input('COURSE    : ')
    print(end =' ' * 50)
    level:str = input('LEVEL     : ')

    if idno != "" and lastname != "" and firstname != "" and course != "" and level != "":
        student:dict = {
            'idno' : idno,
            'lastname' : lastname,
            'firstname' : firstname,
            'course' : course,
            'level' : level,
        }
        students[index] = student
        print('STUDENT UPDATED!'.center(CONSOLE_WIDTH, ' '))
    else:
        print('STUDENT NOT UPDATED!'.center(CONSOLE_WIDTH, ' '))


def main() -> None:
    option: int = 9999

    while option != 0:
        displaymenu()
        print(end=' ' * 50)

        raw = input("Enter Option(0..5): ")
        if not raw.isdigit():
            print("INVALID OPTION".center(CONSOLE_WIDTH, ' '))
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
            print("INVALID OPTION".center(CONSOLE_WIDTH, ' '))

        if option != 0:
            input("Press Enter to continue...".center(CONSOLE_WIDTH, " "))


if __name__ == "__main__":
    main()