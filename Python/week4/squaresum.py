#!/usr/bin/env python3

def main():
    a = list(range(1,101))
    negyzetosszeg = 0
    osszegnegyzet = 0

    for num in a:
        negyzetosszeg+=num**2
        osszegnegyzet+=num
    print("1-től 100-ig a számok négyzetösszege:",negyzetosszeg)
    print("1-től 100-ig a számok összegének négyzete:",osszegnegyzet**2)
    print("A kettő közti külnöbség:", osszegnegyzet**2-negyzetosszeg)
    

#######################################

if __name__=="__main__":
    main()
