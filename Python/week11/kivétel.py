#!/usr/bin/env python3

def main():
    while True:
        try:
            szam1 = float(input("1. szam: "))
            szam2 = float(input("2. szam: "))
            result = szam1 / szam2
            print('Az osztas eredmenye: {0:.2f}'.format(result))
        except ValueError:
            print("Hiba: Kérem, adja meg a két számot.")
        except ZeroDivisionError:
            print("Hiba: Nullával való osztás nem értelmezett.")
        except (KeyboardInterrupt, EOFError):
            print("Kilépés a programból...")
            break
        print('-' * 10)

#####

if __name__ == "__main__":
    main()