def primpal(szam):

    while(True):
       
        m=int(szam**1/2)+1
        e=1
        k=2
        while e==1 and k<m:
            if szam%k==0:
                e=0
            k+=1
        if k==m:
            if str(szam) == str(szam)[::-1]:
                return str(szam)
       
        szam+=1
            
def main():
    szam = input("Adj meg egy számot!")
    print("A legkissebb palindrom prím: " + primpal(int(szam)))

if __name__ == "__main__":
    main()
