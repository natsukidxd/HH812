'''
    Student List
'''

from os import system
#from studentapi import *

VERTICAL:int = 120
HORIZONTAL:int = 30
index:int = 9999

students:list = [
    {
        'idno' : '1000',
        'lastname' : 'golf',
        'firstname' : 'lima',
        'course' : 'bsit',
        'level' : '3',
    },
    {
        'idno' : '2000',
        'lastname' : 'uniform',
        'firstname' : 'quebec',
        'course' : 'bscs',
        'level' : '3',
    },
    {
        'idno' : '4000',
        'lastname' : 'india',
        'firstname' : 'papa',
        'course' : 'bsit',
        'level' : '2',
    },
    {
        'idno' : '5000',
        'lastname' : 'oscar',
        'firstname' : 'sierra',
        'course' : 'bsit',
        'level' : '1',
    },
]

def title(titletext:str)->None:
    system('cls')
    print(f"{titletext.upper()}".center(VERTICAL, '-'))

def displaylist()->None:
    title('student list')
    header:list = list(students[0].keys())
    [print(f"{head.upper():<20}", end = "") for head in header]
    print()
    print('-' * 120)
    for student in students:
        values:list = list(student.values())
        [print(f"{val.upper():<20}", end = "") for val in values]
        print()

    print('NOTHING FOLLOWS'.center(VERTICAL, '-'))

def addstudent()->None:
    global students
    title('add student')
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

    #input validation
    if idno != "" and lastname != "" and firstname != "" and course != "" and level != "":
        student:dict = {
            'idno' : idno,
            'lastname' : lastname,
            'firstname' : firstname,
            'course' : course,
            'level' : level,
        }
        students.append(student)
        print()
        print('NEW STUDENT ADDED'.center(VERTICAL, ' '))
    else:
        print()
        print("FILL ALL FIELDS".center(VERTICAL, ' '))

def findstudent()->None:
    global index
    title('find student')
    print(end =' ' * 50)
    idno:str = input("Enter IDNO: ")
    student:dict={}
    for student in students:
        if student['idno'] == idno:
            index = students.index(student)
            break
    
    if index != 9999:
        system('cls')
        title('find student')
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
        index = 9999

def deletestudent()->None:
    findstudent()
    if index != 9999:
        message:str = "Are you sure you want to delete (Y/N) : "
        inputspaces:int = int((VERTICAL - len(message)) / 2)
        print(end = ' ' * inputspaces)
        option:str = input(message)
        print()
        if option.upper() == "Y":
            students.pop(index)
            print('Student Deleted'.center(VERTICAL, ' '))
        else:
            print('Student Not Deleted'.center(VERTICAL, ' '))

def displaymenu()->None:
    system('cls')
    menuitems:list = [
        "1. DISPLAY ALL STUDENT ",
        "2. FIND STUDENT        ",
        "3. ADD STUDENT         ",
        "4. DELETE STUDENT      ",
        "5. UPDATE STUDENT      ",
        "0. QUIT/END            ",
    ]

    [print() for i in range(0,15-len(menuitems))]
    print('=' * VERTICAL)
    print("MENU".center(VERTICAL, " "))
    print('=' * VERTICAL)
    print()
    [print(menuitems[i].center(VERTICAL,' ')) for i in range(0,len(menuitems))]

def updatestudent()->bool:
    title('update student')
    findstudent()
    print()
    print('UPDATING STUDENT')

    print(end =' ' * 50)
    lastname:str = input('LASTNAME  : ')
    print(end =' ' * 50)
    firstname:str = input('FIRSTNAME : ')
    print(end =' ' * 50)
    course:str = input('COURSE    : ')
    print(end =' ' * 50)
    level:str = input('LEVEL     : ')

    if lastname != "" and firstname != "" and course != "" and level != "":
        student:dict = {
            'lastname' : lastname,
            'firstname' : firstname,
            'course' : course,
            'level' : level,
        }
        students[index] = student
        print('Student updated!')
    
    else:
        print('Student not updated!')

def main()->None:
    option:int = 9999
    while option != 0:
        displaymenu()
        print(end =' ' * 50)
        option:int = int(input("Enter Option(0..6): "))
        if option == 1: displaylist()
        elif option == 2: findstudent()
        elif option == 3: addstudent()
        elif option == 4: deletestudent()
        elif option == 5: updatestudent()
        elif option == 0: print("program ended".center(VERTICAL))
        input("Press any to continue...".center(VERTICAL, " "))

if __name__ == "__main__":
    main() 