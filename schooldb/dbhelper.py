from sqlite3 import connect,Row

database:str = "school.db"

def getall(sql:str,vals:list)->list:
    print(sql)
    conn:any = None
    cursor:any = None
    data:list = []
    try:
        conn = connect(database)
        conn.row_factory = Row
        cursor = conn.cursor()
        cursor.execute(sql,vals)
        data=cursor.fetchall()
    except Exception as ex:
        print(f"Error : {ex}")
    finally:
        cursor.close()
        conn.close()
    return data

def getrecord(idno:str)->list:
    sql:str = "SELECT * FROM `students` WHERE `idno`=?"
    return getall(sql,[idno])

def main()->None:
    # sql:str = "SELECT * FROM `students`"
    students:list = addrecord('1003', 'ferrer', 'krist dave', 'bsit', '3')
    for student in students:
        print(f"{student['idno']:<10} {student['lastname'].upper():<25} {student['firstname'].upper():<25} {student['course'].upper():<10} {student['level'].upper():<5}")

if __name__=="__main__":
    main()
