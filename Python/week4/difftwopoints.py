#!/usr/bin/env python3

import math


def distance(p1, p2):
    distanc = math.sqrt( ((int(p1[0])-int(p2[0]))**2)+((int(p1[1])-int(p2[1]))**2) )
    return distanc


def main():
    p1 = (1, 2)
    p2 = (6, 5)
    print("A" ,p1,"pont és",p2,"pont közti távolság:") 
    print(distance(p1, p2))

#############################################################################

if __name__ == "__main__":
    main()
