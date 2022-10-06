from database_handler import database_handler

def initial_categories_insertion(db_handler):
    db_handler.create_category('Nuetzliches', cur)
    db_handler.create_category('Deko', cur)
    db_handler.create_category('Benchmark', cur)
    db_handler.create_category('Spiele', cur)

    return


if __name__ == '__main__':
    db_path = 'database'
    db_file = 'cad_lib.db'
    db_handler = database_handler(db_path, db_file)
    conn = db_handler.connect2db()

    with conn:
        cur = conn.cursor()

        #Initial creation of tables
        #struct_file = 'create_db.sql'
        #db_handler.create_db_struct_from_file(struct_file, cur)
        #initial_categories_insertion(db_handler)

        cur.execute("SELECT * FROM Categories")
        rows = cur.fetchall()
        for row in rows:
            print(row)









    
    # TEST EINGABE UNSO 
    #conn = db_handler.connect2db()
    #
    #table_creation_string = """CREATE TABLE Test (
    #    TestID int,
    #    TestVar1 varchar(255),
    #    TestVar2 varchar(255)
    #    );"""
    #    
    #table_insert_string = """INSERT INTO Test VALUES (1, 'test1', 'test2');"""
    #
    #if conn:
    #    conn.execute(table_creation_string)
    #    conn.execute(table_insert_string)
    #    conn.execute('SELECT * from Test;')
    #
    #    cur = conn.cursor()
    #    
    #    cur.execute(table_insert_string)
    #    conn.commit()
    #    cur.execute("SELECT * FROM Test")
#
    #    rows = cur.fetchall()
#
    #    for row in rows:
    #        print(row)
    #
    #else:
    #    print('No conn')