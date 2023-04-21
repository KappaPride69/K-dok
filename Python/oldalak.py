def main():
    lista = []
    finallist = []
    valt = "1-4,7,9,11-15"
    index = 0
    for i in range(len(valt)):
        if valt[i] == ',':
           lista.append(valt[index:i])
           index = i+1
    lista.append(valt[index:])
    
    for s in lista:
        if '-' in s:
            finallist.extend(range(int(s[0:s.index('-')]),int(s[s.index('-')+1:])+1))
        else:
            finallist.append(s)
    print(finallist)

if __name__ == "__main__":
    main()