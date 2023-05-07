#!/usr/bin/env python3

def main():
    cells = [False] * 600


    for i in range(1, 601):
        for j in range(i - 1, 600, i):
            cells[j] = not cells[j]

  
    released = [i + 1 for i, state in enumerate(cells) if state]

    
    print("Azoknak az elítélteknek az indexei, akik szabadon távozhatnak:", released)
    #####

if __name__ == "__main__":
    main()