#!/usr/bin/env python3
def stripf(s):
    s=s.replace(" ","")
    s=s.replace("\t","")
    s=s.replace("\n","")
    s=s.replace("\v","")
    s=s.replace("\f","")
    s=s.replace("\r","")
    return s
def main():
    
    s="192.20.246.138:\n \t24263"
    print("A sztring :"+s)
    s=stripf(s)
    print(s)


#######################################

if __name__=="__main__":
    main()
