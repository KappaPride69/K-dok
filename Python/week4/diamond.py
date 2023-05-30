#!/usr/bin/env python3

def main():
    h = int(input("Add meg a gyemant magassagat:"))

    for i in range(h//2+1):
        print(" "*(h//2-i), "*"*(i*2+1))
    for i in range(h//2-1, -1, -1):
        print(" "*(h//2-i), "*"*(i*2+1))


#######################################

if __name__=="__main__":
    main()
