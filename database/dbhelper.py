from sqlite3 import connect, Row

database_name: str = "school.db"


def getprocess(sql: str, values: list) -> list:
    conn: any = None
    cursor: any = None
    data: list = []
    try:
        conn = connect(database)
        conn.row_factory = Row
        cursor = conn.cursor()
        cursor.execute(sql, values)
        data = cursor.fetchall()
    except Exception as ex:
        print(f"Error: {ex}")
    finally:
        cursor.close()
        conn.close()
    return data


def postprocess(sql: str, values: list) -> bool:
    pass


def getall(table: str) -> list:
    sql_cmd: str = f"SELECT * FROM `{table}`"
    return getprocess(sql_cmd, [])


def getrecord(table: str, **kwargs) -> list:
    # SELECT * FROM `students` WHERE `lastname` = ? AND `firstname` = ?
    keys: list = list(kwargs.keys())
    values: list = list(kwargs.values())
    fields: list = []
    [fields.append(f"`{key}` = ?") for key in keys]
    if len(keys) > 1: 
        field: str = fields.join(" AND ")
    sql_cmd = f"SELECT  * FROM `{field}`"
    return getprocess(sql_cmd, values)


def deleterecord(table: str, **kwargs) -> bool:
    # DELETE FROM `students` WHERE `idno` = ?
    keys: list = list(kwargs.keys())
    values: list = list(kwargs.values())
    fields: list = []
    [fields.append(f"`{key}` = ?") for key in keys]
    if len(keys) > 1:
        field: str = fields.join(" AND ")
    sql_cmd = f"DELETE FROM `{field}`"
    return postprocess(sql_cmd, values)


def addrecord(table: str, **kwargs) -> bool:
    pass


def updaterecord(table: str, **kwargs) -> bool:
    pass
