#from msilib.schema import tables
import sqlite3

def create_db(db_name, path):
    return

def connect2db(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        return conn
    except Error as e:
        print(e)
        return None


if __name__ == '__main__':
    db_file = 'database/cad_lib.db'
    conn = connect2db(db_file)
    
    table_creation_string = """CREATE TABLE Test (
        TestID int,
        TestVar1 varchar(255),
        TestVar2 varchar(255)
        );"""
        
    table_insert_string = """INSERT INTO Test VALUES (1, 'test1', 'test2');"""
    
    if conn:
        #conn.execute(table_creation_string)
        #conn.execute(table_insert_string)
        #conn.execute('SELECT * from Test;')
    
        cur = conn.cursor()
        
        #cur.execute(table_insert_string)
        #conn.commit()
        cur.execute("SELECT * FROM Test")

        rows = cur.fetchall()

        for row in rows:
            print(row)
    
    else:
        print('No conn')