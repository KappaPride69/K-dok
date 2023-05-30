#!/usr/bin/env python3
def DefHangrend(s):
    MELY_MGHK = 'aáoóuú'
    MAGAS_MGHK = 'eéiíöőüű'
     
    mahang=0
    mehang=0

    for c in s:
        for tmp in MELY_MGHK:
            if c == tmp:
                mehang+=1 
    for c in s:
            for tmp in MAGAS_MGHK:
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
