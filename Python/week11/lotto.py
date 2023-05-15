import functools
import itertools




# Az összeg és a szorzat alapján meghatározzuk az ismeretlen számokat
def main():
    asd = "141231"
    asd.isnumeric()
    for combo in itertools.combinations(range(1, 46), 6):
        if sum(combo) == 90 and functools.reduce(lambda x, y: x*y, combo) == 996300:
            winner_numbers = combo
            break

    # Az eredmény kiírása
    print("A nyerőszámok: {}".format(sorted(winner_numbers)))

    # Futási idő ellenőrzés
if __name__ == "__main__":
    main()