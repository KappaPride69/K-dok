#!/usr/bin/env python3

from re import sub


def main():
    a = [1,4,2,3,7,5,3,6,3,2,2]
    b=[[a[0]]]
    a.sort()
    for element in a:
        for  sublist in b:
            swt = False
            for subel in sublist:
                if element - subel > 1:
                    b.append([element])
                    swt = True
                    break
        if swt == False:
            sublist.append(element)
                
                        
                   
                    
    print(b)

#######################################

if __name__=="__main__":
    main()
