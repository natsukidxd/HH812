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

def getall()->list:
    return students

def getstudent(idno:str)->dict:
    message:str = 'student not found'
    if len(students)>0:
        for student in students:
            values:list = list(student.values())
            if values[0] == idno:
                message = 'student found'
                return student
            break

    else:
        return message
    
def addstudent(**kwargs)->bool:
    student:dict = kwargs
    students.append(student)
    return 'New Student added'

def deletestudent(idno:str)->bool:
    student:dict = getstudent(idno)
    index:int = students.index(student)
    students.pop(index)
    return f'Student idno:{idno} Deleted'

def updatestudent(**kwargs)->bool:
    idno:str = kwargs['idno']
    student:dict = getstudent(idno)

    if student != 'student not found':
        index:int = students.index(student)
        students[index] = kwargs
        return f'Student idno:{idno} Updated'
    else:
        return 'student not found'
    
