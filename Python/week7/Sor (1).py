#!/usr/bin/env python3

class SOR:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def append(self, item):
        self.items.insert(0,item)

    def popleft(self):
        if self.items:
            return self.items.pop()
        else:
            return None 


    def size(self):
        return len(self.items)
    def __str__(self):
        return str(self.items)

def main():
    sor = SOR()      
    print("SOR kiiratás")    
    print(sor)  
    print("SOR üres e")          
    print(sor.isEmpty())  
    sor.append(1)
    sor.append(4)
    sor.append(5)
    sor.append(4)
    sor.append(5)
    print("SOR kiiratás")   
    print(sor)         
    print("SOR mérete")
    print(sor.size()) 
    print("SOR üres e")  
    print(sor.isEmpty())  
    x = sor.popleft()
    print("SOR elem:")
    print(x)     
    print("SOR kiiratás")   
    print(sor)         
    sor.popleft()
    sor.popleft()      
    x = sor.popleft()
    print("SOR elem:")
    print(x)        

    ##################################################
if __name__=="__main__":
    main()