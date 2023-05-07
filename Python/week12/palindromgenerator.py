import json

def is_palindrome(n):
    return str(n) == str(n)[::-1]

with open('primes.json', 'r') as f:
    primes = json.load(f)

palindrome_primes = [p for p in primes if is_palindrome(p)]
for p in palindrome_primes:
    print(p)

print("Talált palindróm prímek száma:", len(palindrome_primes))