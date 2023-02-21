import requests
from init import Init
from draft import Draft
import sqlite3
from config import databaseFileName
if __name__ == "__main__":
    init = Init()
    init.initialize()
    testDraft = Draft()
    response = testDraft.getPossibleDraft(["Hoodwink","Silencer"])
    conn = sqlite3.connect(databaseFileName)
    c = conn.cursor()
    result = []
    for hero in response:
        id = hero['hero_id']
        winrate = format(hero['wins']/hero['games_played'],'.2f')
        params = (id,)
        checkHeroName = "SELECT heroes.name FROM heroes WHERE id=?"
        c.execute(checkHeroName,params)
        name = c.fetchall()
        result.append({'name':name[0],'winrate':float(winrate)*100.00})
    print(result[:10])
    