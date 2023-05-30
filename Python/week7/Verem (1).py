#!/usr/bin/env python3

class Verem:
    def __init__(self):
        self.elements = []

    def betesz(self, data):
        self.elements.append(data)

    def kivesz(self):
        if self.elements:
            return self.elements.pop()
        else:
            return None 

    def ures(self):
        return True if self.meret() == 0 else False
    
    def meret(self):
        return len(self.elements)
    
    def __str__(self):
        return str(self.elements)

def main():
    v = Verem()      # üres verem létrehozása
    print(v)         # [
    print(v.ures())  # True
    v.betesz(1)
    v.betesz(4)
    v.betesz(5)
    print(v)         # [1 4 5
    print(v.meret()) # 3
    print(v.ures())  # False
    x = v.kivesz()
    print(x)         # 5
    print(v)         # [1 4
    v.kivesz()
    v.kivesz()       # most már üres
    x = v.kivesz()
    print(x)         # None (jelezzük pl. így, hogy egy üres veremből akarunk kivenni)


##################################################
if __name__=="__main__":
    main()
