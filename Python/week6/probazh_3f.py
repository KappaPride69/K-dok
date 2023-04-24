#! /usr/bin/env python3
import sys
def karakter_szamlalo(Szo):
    diction = {}
    for c in Szo:
        if c not in diction:
            diction.update({c:1})
        else:
            diction[c]+=1
    return diction
def main():
    
    if len(sys.argv) > 2:
        print("Hiba! A program csak egyetlen egy parancssori argumentumot fogad el!")
        exit(1)
    elif len(sys.argv) == 1:
        print("Hiba! A programnak kötelező megadni egy parancssori argumentumot!")
        exit(1)
    else:
        eredmeny = karakter_szamlalo(sys.argv[1])
        keylist = list(eredmeny.keys())
        for i in range(len(eredmeny)):
            print(keylist[i] + "-" + str(eredmeny[keylist[i]]))
    
        

if __name__ == "__main__":
    main()