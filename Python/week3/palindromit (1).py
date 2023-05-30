#!/usr/bin/env python3

def main():
    name=input("Adj meg egy szót: ")
    name=name.strip()
    i=0
  
    while i<len(name):
        
        if name[i]==name[len(name)-1-i]:
            i+=1
        else:
            print("Nem palindrom")
            exit(0)
    print("A szó palidnrom")

#######################################

if __name__=="__main__":
    main()