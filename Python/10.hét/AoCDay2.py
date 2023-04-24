#!/usr/bin/env python3

def main():
    szamok = []
    INPUT="/home/ricsi/szkript/day02.txt"
    
    F1=open(INPUT,"r")
    
    for line in F1:
        szamok.append([int(i) for i in line.split()])

    first = sum(max(line) - min(line) for line in szamok)

    second = 0
    for line in szamok:
        for a in line:
            for b in line:
                if a % b == 0 and a != b:
                    second += a // b
    F1.close()
    print("Az ellenörző összeg: "+str(first))
#######################################

if __name__=="__main__":
    main()
