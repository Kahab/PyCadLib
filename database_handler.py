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

    def create_table(self, table):
        return

    def create_entry(self, entry):
        return

    def return_tables(self):
        return

    def return_table_content(self, table):
        return

    def create_db_struct_from_file(self, struct_file):
        conn = self.connect2db()
        cur = conn.cursor()
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