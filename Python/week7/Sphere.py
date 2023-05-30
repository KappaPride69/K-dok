#!/usr/bin/env python3

import math


class   Sphere:
    def __init__(self,radius):
        
        self.radius = radius
        self.PI=math.pi
    
    def area(self):
        return 4*self.PI*(self.radius*self.radius)
    
    def volume(self):
        
        return (4*self.radius*self.radius*self.radius*self.PI)/3
    
    def __lt__(self,other):
        return self.area() < other.area()
    
    def __gt__(self,other):
        return self.area() > other.area()
    
    def __le__(self,other):
        return self.area() <= other.area()
    
    def __ge__(self,other):
        return self.area()  >= other.area()


    
    
        
    def __str__(self):
      
        return "Sphere({r})".format(r=self.radius)

def main():
    r1 = Sphere(10)
    r2 = Sphere(15)
    
    print( "{kor1} felszííne nagyobb e mint {kor2}:".format(kor1 = r1, kor2 = r2))
    print(r1 < r2)
    print( "{kor1} felszííne kissebb e mint {kor2}:".format(kor1 = r1, kor2 = r2))
    print(r1 > r2)
    print( "{kor1} felszííne kissebb egyenlő e {kor2}-val(-vel):".format(kor1 = r1, kor2 = r2))
    print(r1 <= r2)
    print( "{kor1} felszííne nagyobb egyenlő e {kor2}-val(-vel):".format(kor1 = r1, kor2 = r2))
    print(r1 >= r2)




##################################################
if __name__=="__main__":
    main()
