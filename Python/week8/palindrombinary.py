def main():
    sum = 0
    for i in range(1,1000000):
        if str(i) == str(i)[::-1] and str(bin(i))[2:] == str(bin(i))[:1:-1]:
            sum+=i
    print(sum)
    asd = 15*175555+15*850000+15*20000
    print(asd)

if __name__ == "__main__":
    main()