#!/usr/bin/env python3
from cgi import print_form


def hello(name,color,what):
    #printf("%s, %s az %s\n", name, color, what)
    print("{0}, {1} az {2}".format(name,color,what))
    print("{}, {} az {}".format(name,color,what))
    print("{nev}, {szin} az {mi}".format(nev = name, szin = color, mi = what))
    print(f"{name.capitalize()}, {color} az {what}")
    
    
    
def main():
    #hello("ricsi","kék","ég")
    valami = "Valami"
    print(valami[::2])
    s = r"Python\n\n\n\n"
    print(s)

#######################################

if __name__=="__main__":
    main()
