from filemanager import *


def getall() -> list:
    data: list = loader()
    return data


def getrecord(idno: str) -> tuple:
    data: list = getall()
    for item in data:
        value: list = list(item.values())
        if idno == value[0]:
            return item, data.index(item)

    return {}, -1


def deleterecord(idno: str) -> bool:
    students: list = getall()
    ok: bool = False
    data_str, index_str = getrecord(idno)
    student_data: dict = dict(data_str)
    student_index: int = int(index_str)
    if data != {}:
        print(student_data)
        print(student_index)
        option: str = input("Delete this (Y/N)?: ")
        if option.upper() == "Y":
            students.pop(student_index)
            updater(students)
            ok = True
            return ok
    else:
        print('No student found')
    return ok


def addrecord(**kwargs) -> bool:
    pass


deleterecord("20000000")
