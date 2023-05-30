#!/usr/bin/env python3
from re import A
from dbus import DBusException


DIC=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
DICSMMALL=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
MESSAGE="""Cbcq Dgyk!

Dmeybh kce cew yrwyg hmrylyaqmr:
rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!

Aqmimjjyi:

Ynyb"""
def translate(c):
    i=0
    
    while i < len(DIC):
        if c.isupper():
            if c == DIC[i] and i < len(DIC)-2:
                
                
                c=DIC[i+2]
                return c
            if c == "Y":
                return "A"
            i+=1 
        else:
            if c == DICSMMALL[i]:
                
                if i < len(DICSMMALL)-2:
                    c=DICSMMALL[i+2]
                    return c
                if c == "y":
                    return "a"
            i+=1
        
    

    return c
def main():
    Decypt=""
    for c in MESSAGE:
        Decypt+=translate(c)
    print(Decypt)
#######################################

if __name__=="__main__":
    main()