#!/usr/bin/env python3


#Megadja hogy az egymást követő megegyező számjegyek összege mennyi
def main():
    a = input("Adjon meg egy számsorozatot:")
    a=str(a)
    sum=0
    i = 1
    for c in a:
        if i <= len(a)-1 and c == a[i]:
            
            sum+=int(c)
        i+=1

    if a[len(a)-1] == a[0]:
        sum+=(int(a[len(a)-1]))
    print("Az eredmény:")
    print(sum)
    
           
    

    
#######################################

if __name__=="__main__":
    main()
