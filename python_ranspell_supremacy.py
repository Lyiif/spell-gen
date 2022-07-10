import csv

import os
import random

from flask import Flask

app = Flask(__name__)




n=0
csvfilepath = "Spells.csv"
availableSpells = []
spellsknown = 7
maxspellslot = 3
selectedClass = "Warlock"
availableCantrips = []
cantripsKnown = 3
with open(csvfilepath, 'r', encoding="utf8") as file:
    reader = csv.reader(file)
    try:
        for row in reader:
            del row[1]
            del row[2:6]
            del row[4:]
            del row[2]
            n+=1
            if selectedClass in row[2] and row[1][0] != "0" and int(row[1][0])<=maxspellslot:
                availableSpells.append(row)
            if selectedClass in row[2] and row[1][0] == "0" and int(row[1][0])<=maxspellslot:
                availableCantrips.append(row)
    except Exception as e:
        print(e)
    #print("done",n)
    #print(availableSpells)
@app.route("/")
def doit():
    
   
    output1=""
    output2=""
    for i in random.sample(availableSpells, spellsknown):
        output1+=f"[{i[1][0]}]    {i[0]}"+"\n"
    for i in random.sample(availableCantrips, cantripsKnown):
        output2+=f"[*]    {i[0]}"
    return output1 + "\n"+output2
    

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
