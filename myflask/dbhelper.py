from sqlite3 import connect, Row
import os

# Get absolute path to database file relative to this script
script_dir = os.path.dirname(os.path.abspath(__file__))
database: str = os.path.join(script_dir, "myflask.db")


def get_db() -> any:
    """Return a database connection."""
    conn = connect(database)
    conn.row_factory = Row
    return conn

def getprocess(sql: str, vals: list) -> list:
    """Execute a SELECT query and return all matching rows as a list."""
    conn = None
    cursor = None
    data: list = []
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute(sql, vals)
        data = cursor.fetchall()
    except Exception as ex:
        print(f"Error : {ex}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
    return data


def validate_user(username: str, password: str) -> bool:
    """Check if a username/password combination exists in the users table."""
    sql: str = "SELECT * FROM users WHERE username=? AND password=?"
    result: list = getprocess(sql, [username, password])
    return len(result) > 0