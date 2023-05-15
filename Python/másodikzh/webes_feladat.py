
import json
import requests
from pprint import pprint
import re

def find_strongest_hero(hosok_listaja):
    if not hosok_listaja:
        return []
    
    legmagasabb_jatekos = hosok_listaja[0]
    for jatekos_szotara in hosok_listaja:
        if jatekos_szotara["level"] > legmagasabb_jatekos["level"]:
            legmagasabb_jatekos = jatekos_szotara
            
    return legmagasabb_jatekos

def find_hosok(hosok_nevei):
    minta_sztring = r"^[aeiou].*?[bcdfghjklmnpqrstvwxyz]$"
    specialis_nevu_hosok = []
    for hos_neve in hosok_nevei:
        egyezes = re.search(minta_sztring, hos_neve.lower())
        if egyezes:
            specialis_nevu_hosok.append(egyezes.group().capitalize())
            
    return specialis_nevu_hosok

def main():
    url = "https://raw.githubusercontent.com/suvicsabika/szkriptnyelvek_2023_tavasz_02/main/!ZH_FAJLOK!/minta_masodik_zh/players.json"
    keres = requests.get(url)
    szoveg = keres.text
    jatekosok_listaja = json.loads(szoveg)
    
    legerosebb_jatekos = find_strongest_hero(jatekosok_listaja)
    pprint(legerosebb_jatekos, indent=1)
    
    hosok_nevei = []
    for jatekos in jatekosok_listaja:
        hosok_nevei.append(jatekos["name"])
        
    specialis_nevu_hosok = find_hosok(hosok_nevei)
    print(specialis_nevu_hosok)

if __name__ == '__main__':
    main()