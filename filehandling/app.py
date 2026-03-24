from os import system
from ast import literal_eval

filename: str = "students.txt"
students: list = []


def getallstudents() -> None:
    global students
    students.clear()

    file = open(filename, "r")
    for line in file:
        student: dict = literal_eval(line.strip())
        students.append(student)
    file.close()


def findstudent(idno: str) -> None:
    getallstudents()

    for student in students:
        if student["idno"] == idno:
            print("Student found")
            print("ID No.     :", student["idno"])
            print("First Name :", student["firstname"])
            print("Last Name  :", student["lastname"])
            print("Course     :", student["course"])
            print("Level      :", student["level"])
            return

    print("Student Not Found")


def main() -> None:
    system("cls")
    studentid: str = input("Enter id to search: ")
    findstudent(studentid)


if __name__ == "__main__":
    main()
