#!/usr/bin/env python3


class Bag:
    szam = 0
    def __init__(self):
        self.datas = []
        Bag.szam+=1
        
    def add(self,data):
        self.datas.append(data)
        
    def add_twice(self,data):
        self.add(data)
        self.add(data)
    
    def __str__(self):
        return self.datas
       
        
class Greetings:
    def __init__(self,name):
        self.name = name
        
    def say_hi(self):
        print("Hi " + self.name)
    
      
class Hello:
    def create_name(self,name):
        self.name = name
        
    def display_name(self):
        return self.name
    
    def greet(self):
        print("Hello "+self.name)


class MyClass:
    def hello(self):
        return "Hello World!"


def main():
    
    ##obj = MyClass()
    ##print(obj.hello())
    
########################################

    h = Hello()
    h.create_name("Alice")
    print(h.display_name())
    h.greet()
    
########################################

    g = Greetings("Alice")
    g.say_hi()
    
########################################

    b = Bag()
    b.add(5)
    b.add_twice(3)
    print(b.datas)

########################################

if __name__ == "__main__":
    main()