def main():
    sum = 0
    for i in range(1,1000000):
        if str(i) == str(i)[::-1] and str(bin(i))[2:] == str(bin(i))[:1:-1]:
            sum+=i
    print(sum)


if __name__ == "__main__":
    main()