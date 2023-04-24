#!/usr/bin/env python3

class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        

    def meret(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []

class MyQueue(object):

    def __init__(self):

        # Two Stacks
        self.in_stack = Stack()
        self.out_stack = Stack()

    def append(self, item):
        self.in_stack.push(item)
        

    def popleft(self):
        
        if self.out_stack.is_empty:
            while self.in_stack.meret()>0:
                self.out_stack.push(self.in_stack.pop())
               
        backert = self.out_stack.items.pop()
        while self.out_stack.meret()!=0:
             self.in_stack.push(self.out_stack.pop())
            
        return backert
    
    def is_Empty(self):
        
        return True if self.in_stack.meret() == 0  and self.out_stack.meret() ==0 else False

    def size(self):
        return self.in_stack.meret()+self.out_stack.meret()
    

    def __str__(self):
        if self.in_stack.is_empty():
            return str(self.out_stack.items)
        else:
            return str(self.in_stack.items)


def main():
    sor = MyQueue() 
    print("SOR kiiratás")    
    print(sor)  
    print("SOR üres e")          
    print(sor.is_Empty())  
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
    print(sor.is_Empty())  
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
