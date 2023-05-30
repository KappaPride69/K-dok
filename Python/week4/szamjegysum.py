#!/usr/bin/env python3


def main():
    a=list(range(0,101))
    sum=0
    for c in a:
        for tmp in str(c):
            sum+=int(tmp)
    print("0-tól 100-ig a számokjegyek sumja:",sum)

#############################################################################

if __name__ == "__main__":
    main()
