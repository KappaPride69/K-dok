#!/usr/bin/env python3

def main():
    number=input("Adj meg egy számot: ")
    number=number.strip()
    number=number[::-1]
    
    print(number)

#######################################

if __name__=="__main__":
    main()
