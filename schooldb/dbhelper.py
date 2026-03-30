from sqlite3 import connect,Row

database:str = "school.db"

def getprocess(sql:str,vals:list)->list:
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

def getall(table:str)->list:
    sql:str = f"SELECT * FROM `{table}`"
    return getprocess(sql,[])
    
def getrecord(table:str,**kwargs)->list:
    keys:list = list(kwargs.keys())
    vals:list = list(kwargs.values())
    sql:str = f"SELECT * FROM `{table}` WHERE `{keys[0]}`=?"
    return getprocess(sql,vals)

def postprocess(sql:str,vals:list)->bool:
    print(sql)
    conn:any = None
    cursor:any=None
    try:
        conn = connect(database)
        cursor = conn.cursor()
        cursor.execute(sql,vals)
        conn.commit()        
    except Exception as ex:
        conn.rollback()
        print(f"Error : {ex}")
    finally:
        cursor.close()
        conn.close()
    return True if cursor.rowcount>0 else False

def addrecord(table:str,**kwargs)->bool:
    keys:list = list(kwargs.keys())
    vals:list = list(kwargs.values())
    qmark:list = '?'*len(vals)
    flds:str = '`,`'.join(keys)
    dta:str = ','.join(qmark)
    sql:str = f"INSERT INTO `{table}`(`{flds}`) VALUES ({dta})"
    return postprocess(sql,vals)
    
def deleterecord(table:str,**kwargs)->bool:
    keys:list = list(kwargs.keys())
    vals:list = list(kwargs.values())
    sql:str = f"DELETE FROM `{table}` WHERE `{keys[0]}`=?"
    return postprocess(sql,vals)
    
def updaterecord(table:str,**kwargs)->bool:
    #UPDATE `students` SET `lastname`=?,`firstname`=?,`course`=?,`level`=? WHERE `idno`='1000'
    keys:list = list(kwargs.keys())
    vals:list = list(kwargs.values())
    flds:list = []
    newvals:list = []
    for i in range(1,len(keys)):
        flds.append("`"+keys[i]+"`=?")
        newvals.append(vals[i])
    fld:str = ",".join(flds)
    sql:str = f"UPDATE `{table}` SET {fld} WHERE `{keys[0]}`='{vals[0]}'"
    return postprocess(sql,newvals)
        
def main()->None:
    
    students:list = getrecord('students',idno='1000')
    for student in students:
        print(f"{student['lastname'].upper():<25} {student['firstname'].upper():<25}")
if __name__=="__main__":
    main()