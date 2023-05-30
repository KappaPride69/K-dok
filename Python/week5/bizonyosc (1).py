#!/usr/bin/env python3

#Visszaadja az alapértelmezett listában lévő elemeket a szóban ez a lista felülírható
def valid(text, chars='ABCDEFGHIJKLMNOPQRSTUVWXYZ01234567789'):
    strin=""
    for k in text:
        for c in chars:
            if k == c:
                strin+=k
    return strin
        
def main():
    print(valid("Barking!"))
    print(valid("KL754","0123456789"))
    print(valid("kalaaa"))
    
    
           
    

    
#######################################

if __name__=="__main__":
    main()
