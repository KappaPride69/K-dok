#!/usr/bin/env python3
i=0
def rekpalindrom(s,i):
    if i==len(s):
        return True
    if s[i]==s[len(s)-1-i] :
        i+=1
        rekpalindrom(s,i)
    else:
        return False

    return True
def main():
    name=input("Adj meg egy szót: ")
    name=name.strip()
    
    if rekpalindrom(name,i):
        print("A szó palindrom")
    else:
        print("Nem palindrom")


#######################################

if __name__=="__main__":
    main()