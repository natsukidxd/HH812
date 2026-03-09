'''
    Student List
'''

from os import system

VERTICAL:int = 120
HORIZONTAL:int = 30

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

def displaylist()->None:
    system('cls')
    print('STUDENT LIST'.center(VERTICAL, '-'))
    header:list = list(students[0].keys())
    [print(f"{head.upper():<20}", end = "") for head in header]
    print()
    print('-' * 120)
    for student in students:
        values:list = list(student.values())
        [print(f"{val.upper():<20}", end = "") for val in values]
        print()

    print('-' * 120)
    print('NOTHING FOLLOWS'.center(VERTICAL, '-'))

def main()->None:
    displaylist()

if __name__ == "__main__":
    main() 