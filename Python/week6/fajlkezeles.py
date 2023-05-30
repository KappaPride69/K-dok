#!/usr/bin/env python3

def main():

    INPUT="/home/ricsi/Desktop/string1.py"
    OUTPUT="/home/ricsi/Desktop/string1_clean.py"
    F1=open(INPUT,"r")
    F2=open(OUTPUT,"w")
    row=0
    osszrow = 0
    print("Fáfl beolvasása és feldolgozása:")
    for lines in F1:
        osszrow+=1
    F1.close()
    F1=open(INPUT,'r')
    for line in F1:
        if row ==0:
            F2.write(line)
            
            print(str(row/osszrow)+"%")
            
        if line[0] != "#" and not line.strip().startswith('#'):
            F2.write(line)
        row+=1
        percent = (row/osszrow)*100
        print("%.2f"  % percent+ "%")
    
                
            


       
    F1.close()
    F2.close()
    print("Tisztítás...")
    print("Kész!")
 
#######################################

if __name__=="__main__":
    main()

