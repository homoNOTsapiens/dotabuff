import sqlite3
import requests
import json
class Database():
    def __init__(self,databaseFileName):
        self.databaseFileName = databaseFileName
    def createDB(self):
        conn = sqlite3.connect(self.databaseFileName)
        c = conn.cursor()
        createHeroesTable = """CREATE TABLE IF NOT EXISTS heroes (
                                    id INTEGER,
                                    name TEXT NOT NULL
        )"""
        c.execute(createHeroesTable)
        conn.commit()
        c.close()
        conn.close()
    def fillDB(self):
        conn = sqlite3.connect(self.databaseFileName)
        c = conn.cursor()
        heroesList = requests.get("https://api.opendota.com/api/heroes").json()
        for hero in heroesList:
            heroId = hero['id']
            heroName = hero['localized_name'].replace("-","")
            params = (heroId,heroName)
            updateHeroesTable = "INSERT INTO heroes(id,name) VALUES (?,?)"
            c.execute(updateHeroesTable,params)
        conn.commit()
        c.close()
        conn.close()
