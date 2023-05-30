#!/usr/bin/env python3

import sys
import random as r

UPTO = 100


def main():
    tmp = 1
    for i in range(UPTO):
        
        if i+1<10*tmp:
            
            print(r.randint(0, 9), end="")
        else:
           
            print(r.randint(0, 9), end="\n")
            tmp+=1

    

#######################################

if __name__=="__main__":
    main()