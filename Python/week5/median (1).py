#!/usr/bin/env python3
def test(a):
    median = 0
    medlist=sorted(a)
    if len(medlist)%2==0:
        median = (medlist[len(medlist)//2-1]+medlist[len(medlist)//2])/2
       
    
    else:
        median = medlist[len(medlist)//2]
        
    print("Az ",a," medianja:",median )

def main():
    
    test([1, 2, 3, 4, 5])
    test([3, 1, 2, 5, 3])
    test([1, 300, 2, 200, 1])
    test([3, 6, 20, 99, 10, 15])
#######################################

if __name__=="__main__":
    main()

