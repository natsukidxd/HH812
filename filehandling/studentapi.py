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
    students = getall()
    student_data, student_index = getrecord(idno)

    if student_index != -1:
        print(f"Found: {student_data}")
        option = input("Are you sure you want to delete this student? (Y/N): ")
        if option.upper() == "Y":
            students.pop(student_index)
            updater(students)
            print("Record deleted successfully.")
            return True
    else:
        print("No student found")
    return False


def addrecord(**kwargs) -> bool:
    pass


deleterecord("20000000")
