#!/usr/bin/env python3

#Alapértelmezettként be van állítva egy False érték így nem fut le az extra rész viszont ha ezt megváltoztatja True-ra akkor lefut a debuggolós rész
def loop(n, debug = False):
    if debug == False:
        for i in range(1,n+1):
            print(i, end = " ")
        print("")
    else:
        print("#ciklus kezdete:")
        for i in range(1,n+1):
            print(i, end = " "),
        print("")
        print("#ciklus vége")
def main():
    
    loop(5)
    loop(5,True)
#######################################

if __name__=="__main__":
    main()
