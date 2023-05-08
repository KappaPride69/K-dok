#!/usr/bin/env python3

import re


def find(keresett,sztring):
    m = re.search(keresett,sztring)
    if m:
        print(m.group())
    else:
        print("Nincs benne!")


def main():
    s = "regularis kifejezesek"
    keresett = "reg"
    m = re.search(keresett,s)
    print(m)
    print(m.span())
    keresett2 = "fds"
    ser = re.search(keresett2,s)
    print(ser)
    find("reg","regularis")
    find("fda","alma")

   

if __name__ == "__main__":
    main()