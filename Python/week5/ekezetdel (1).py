#!/usr/bin/env python3

def main():
    text = """

"A katalán zászló, a Senyera színeit fogja viselni a következő idény során a spanyol élvonalban szereplő FC Barcelona labdarúgócsapata.

A Marca című sportnapilap hétfői internetes kiadása szerint az együttes játékosai az idegenbeli mérkőzéseken húzzák majd magukra a sárga-piros csíkozású mezt - első ízben a klub történelme során.

A döntés várhatóan nem marad politikai visszhang nélkül Spanyolországban, tekintettel a katalán önállósodási törekvésekre." """
    
    
    dict={"á":"a",
        "é":"e",
        "í":"i",
        "ó":"o",
        "ü":"u",
        "ö":"o",
        "ű":"u",
        "ú":"u",
        "ő":"o",
        "Á":"A",
        "É":"E",
        "Í":"I",
        "Ó":"O",
        "Ü":"U",
        "Ö":"O",
        "Ű":"U",
        "Ú":"U",
        "Ő":"O"
    }
    newtext=""""""
    for w in text:
        if w in dict:
            newtext+=dict[w]
        else:
            newtext+=w
    print(newtext)
    
#######################################

if __name__=="__main__":
    main()