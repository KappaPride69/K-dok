#!/usr/bin/env python3

from enum import Enum

class Hangrend(Enum):
    MELY_MGHK = 'aáoóuú'
    MAGAS_MGHK = 'eéiíöőüű'

def DefHangrend(s):
    mahang=0
    mehang=0

    for c in s:
        for tmp in Hangrend.MELY_MGHK.value:
            if c == tmp:
                mehang+=1 
    for c in s:
            for tmp in Hangrend.MAGAS_MGHK.value:
                if c == tmp:
                    mahang+=1 
    if mehang == 0 and mahang > 0:
        return "magas"
    if mehang > 0 and mahang == 0:
        return "mély"
    if mehang > 0 and mahang > 0:
        return "vegyes"
    
    return "semmilyen" 


def main():

    words = ["ablak", "erkély", "kisvasút", "magas", "mély","pfff"]
    
    for s in words:
        print("A(z)", s , DefHangrend(s), "hangrendű szó!")

#############################################################################

if __name__ == "__main__":
    main()
