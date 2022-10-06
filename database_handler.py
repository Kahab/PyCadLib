#from msilib.schema import tables
import sqlite3
import os

class database_handler:
    def __init__(self, db_path, db_name):
        self.db_path =  os.path.join(os.getcwd(), db_path)
        self.db_name = db_name

    def create_db(self):
        # db_name aufsplitten in name/path , bzw generell path und name trennen
        # Wenn in exception unten und no conn , dann pfad erstellen 
        return

    def create_path(self, path):
        try:
            os.makedirs(path)
            print('Succesfully created directory.')
            return
        except:
            print('Error creating directory')
            return
        

    def checkPath(self, path):
        if (os.path.exists(path)):
            return True
        else:
            return False

    def connect2db(self):
        """ create a database connection to a SQLite database """
        if (self.checkPath(self.db_path)):
            print('Path to BD found.')
        else:
            self.create_path(self.db_path)
        conn = None
        try:
            db_full_path = os.path.join(self.db_path, self.db_name)
            conn = sqlite3.connect(db_full_path)
            print(sqlite3.version)
            return conn
        except Exception as e:
            print(e)
            # Create db aufrufen byw create path schreiben
            return None

    def create_table(self, cur, table_name, cols):
        # Cols should be dictionary of {name: datatype, [constraints]}
        table_creation_string = f"""CREAATE TABLE {table_name} ("""
        for column_name, (datatype, constraints) in cols:
            table_creation_string += f"""{column_name}"""
            for constraint in constraints:
                table_creation_string += f""" {constraint}"""
            table_creation_string += f""","""
        table_creation_string += ');'
        
        cur.execute(table_creation_string)

        return

    def create_entry(self, entry, cur):
        name = entry.get_name()
        category = entry.get_catID()
        files = entry.get_fileID()
        tags = entry.get_tags()
        entry_creation_string = f"""INSERT INTO Collection (CatID, FileID, Tags, Name_desc) VALUES ({category}, {files}, {tags}, {name});"""

        cur.execute(entry_creation_string)
        
        return

    def create_category(self, cat_name, cur):
        cat_creation_string = f"""INSERT INTO Categories (Name) VALUES ('{cat_name}');"""
        cur.execute(cat_creation_string)
        return

    def create_file_entry(self, files):
        counter = 0
        file_entry_string = f"""INSERT INTO Files ("""
        for file in files:
            counter += 1
            if not file == files[-1]:
                file_entry_string += f'File{counter},'
            else:
                file_entry_string += f'File{counter})'

        file_entry_string += f' VALUES ('

        for file in files:
            if not file == files[-1]:
                file_entry_string += f'{file}, '
            else:
                file_entry_string += f'{file}); '

        return

    def return_tables(self, cur):
        cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
        print(cur.fetchall())
        return

    def return_table_content(self, cur, table):
        cur.execute(f"SELECT * FROM {table}")
        rows = cur.fetchall()
        for row in rows:
            print(row)
        return

    def create_db_struct_from_file(self, struct_file, cur):
        #conn = self.connect2db()
        #cur = conn.cursor()
        sqlFile = None
        with open (struct_file, 'r') as fd:
            sqlFile = fd.read()

        sqlCommands = sqlFile.split(';')

        for command in sqlCommands:
            try:
                cur.execute(command)
            except sqlite3.OperationalError as msg:
                print("Command skipped: ", msg)


if __name__ == '__main__':
    print("I shouldnt be a main executable")