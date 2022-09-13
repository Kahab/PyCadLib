import sqlite3

def create_db(db_name, path):
    return

def connect2db(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    db_file = 'database/cad_lib.db'
    connect2db(db_file)
    
    