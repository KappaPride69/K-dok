#!/usr/bin/env python3
def palindrom(s):
    return s==s[::-1]
def main():
    name=input("Adj meg egy szót: ")
    name=name.strip()
    ans = palindrom(name)
    if ans:
        print("A szó palindrom")
    else:
        print("Nem palindrom")

#######################################

if __name__=="__main__":
    main()