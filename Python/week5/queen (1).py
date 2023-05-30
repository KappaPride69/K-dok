#!/usr/bin/env python3
def queenprint(l):
    newl=[]
    for n in l:
        newl.append(7-n)
    
    print("+-----------------+")
    for i in range(0,8):
        line="| "
        for j in range(0,8):
            
            if newl[j] == i:
                line+="Q "
            else:
                line+=". "
        line+="|"
        print(line)
            

        
    print("+-----------------+")


def main():
    queenprint([0,4,7,5,2,6,1,3])
    
    
   
    

    
#######################################

if __name__=="__main__":
    main()
