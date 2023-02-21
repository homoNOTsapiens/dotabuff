import requests
import os.path
import sqlite3
from config import databaseFileName
import random
class Draft():
    def isHeroesValide(self,currentDraft:list):
        isValid = True
        if currentDraft:
            if os.path.isfile(databaseFileName):
                conn = sqlite3.connect(databaseFileName)
                c = conn.cursor()
                for hero in currentDraft:
                    print (hero)
                    if hero:
                        name = hero.replace("-","")
                        params = (name,)
                        checkHero = "SELECT * FROM heroes WHERE name=?"
                        c.execute(checkHero,params)
                        records = c.fetchall()
                        if records:
                            isValid = True
                        else:
                            isValid = False
                            c.close()
                            conn.close()
                            return isValid
                c.close()
                conn.close()
                return isValid
            else:
                print("database does not exist")
        else:
            return False
    def getPossibleDraft(self,currentDraft):
        if self.isHeroesValide(currentDraft):
            conn = sqlite3.connect(databaseFileName)
            c = conn.cursor()
            possibleDraft = []
            result = []
            for hero in currentDraft:
                name = hero.replace("-","")
                params = (name,)
                getHeroId="SELECT heroes.id FROM heroes WHERE name=?"
                c.execute(getHeroId,params)
                record = c.fetchall()
                possibleDraft= possibleDraft + requests.get(f"https://api.opendota.com/api/heroes/{record[0][0]}/matchups").json()
                result = result + sorts(possibleDraft)
            result = sorts(result)
            c.close()
            conn.close()
            result= {x['hero_id']: x for x in result}.values()
            return result
        else:
            return None
def sorts(possibleDraftUnsorted):
    for i in range(len(possibleDraftUnsorted)-1):
        for j in range(len(possibleDraftUnsorted)-i-1):
            if possibleDraftUnsorted[j]['wins']/possibleDraftUnsorted[j]['games_played'] > possibleDraftUnsorted[j+1]['wins']/possibleDraftUnsorted[j+1]['games_played']:
                possibleDraftUnsorted[j], possibleDraftUnsorted[j+1] = possibleDraftUnsorted[j+1], possibleDraftUnsorted[j]
    return possibleDraftUnsorted


