import json

def sieve(n):
    primes = [True] * (n + 1)
    primes[0], primes[1] = False, False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i ** 2, n + 1, i):
                primes[j] = False
    return [i for i in range(n + 1) if primes[i]]




def main():
    primes = sieve(10000000)

    with open('primes.json', 'w') as f:
        json.dump(primes, f)
   
if __name__ == "__main__":
    main()