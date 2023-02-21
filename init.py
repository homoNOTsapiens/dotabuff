import os.path
from database import Database
from config import databaseFileName
class Init():
    def initialize(self):
        if os.path.isfile(databaseFileName):
            print(f"{databaseFileName} file exist")
            db = Database(databaseFileName=databaseFileName)
            db.fillDB()
        else:
            print("database.db file does not exist")
            print("creating database")
            db = Database(databaseFileName=databaseFileName)
            db.createDB()
            db.fillDB()


