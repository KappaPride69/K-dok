import re


def main():
    
    with open('corpus.txt', 'r') as f:
        corpus = [line.split(',')[0] for line in f]

    
    matches = re.findall(r"\b\w*J\w*S\w*U\w*N\w*\b", corpus)

 
    print(matches)


if __name__ == "__main__":
    main()