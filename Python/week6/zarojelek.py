#C:\Users\user\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.10
def ervenyes (sor):
      
    kupac = []
    nyito = ('([{')
    zaro = (')]}')
    parok = {')' : '(' , ']' : '[' , '}' : '{'}
    for i in sor:
        if i in nyito:
            kupac.append(i)
        if i in zaro:
            if not kupac:
                return "A(z) " + sor + " nem érvényes"

            if kupac.pop() != parok[i]:
                return "A(z) " + sor + " nem érvényes"
                
            else:
                continue
    if not kupac:
        return "A(z) " + sor + " érvényes"
    else:
        return "A(z) " + sor + " nem érvényes"

def main():
    print(ervenyes("(3+{1-1)})"))
    print(ervenyes("[1+1]+(2*2)-{3/3}"))
    print(ervenyes("(({[(((1)-2)+3)-3]/3}-3)"))

#############################

if __name__=="__main__":
    main()