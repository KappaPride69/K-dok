
import random
import sys

class Hallgato:
    hallgatok = []
    
    def __init__(self, nev, eletkor, szak):
        self.nev = nev.lower().capitalize()
        self.eletkor = eletkor
        self.szak = szak.upper()
    
    @staticmethod
    def szak_hallgato(szak):
        szak_hallgatoi = []
        for hallgato in Hallgato.hallgatok:
            if hallgato.szak == szak.upper():
                szak_hallgatoi.append(hallgato)
        
        return szak_hallgatoi
    
    def random_kodnev(self):
        hallgato_neve = list(self.nev)
        random.shuffle(hallgato_neve)
        
        return str(hallgato_neve)
    
    def __lt__(self, masik):
        return self.eletkor < masik.eletkor

    def __gt__(self, masik):
        return self.eletkor > masik.eletkor
    
    def __str__(self):
        return f"{self.nev}, {self.eletkor} éves {self.szak} hallgató"

def main():
    try:
        with open("nevek.csv", "r", encoding="utf-8") as fajl:
            for sor in fajl:
                sor = sor.rstrip("\n")
                sor_feldarabolva = sor.split(",")
                aktualis_hallgato = Hallgato(sor_feldarabolva[0], sor_feldarabolva[1], sor_feldarabolva[2])
                Hallgato.hallgatok.append(aktualis_hallgato)
    except IOError as fajl_kivetel:
        print(f"Hiba! Fájlkezelési hiba lépett fel, a program futása közben. A hiba üzenet: {fajl_kivetel}", file=sys.stderr)

    legfiatalabb = ""
    try:
        legfiatalabb = Hallgato.hallgatok[0]
        for hallgato in Hallgato.hallgatok:
            if hallgato < legfiatalabb:
                legfiatalabb = hallgato
    except IndexError as lista_ures_kivetel:
        print(f"Hiba! A Hallgato.hallgatok lista üres! Hiba üzenet: {lista_ures_kivetel}", file=sys.stderr)

    legidosebb = ""
    try:
        legidosebb = Hallgato.hallgatok[0]
        for hallgato in Hallgato.hallgatok:
            if hallgato > legidosebb:
                legidosebb = hallgato
    except IndexError as lista_ures_kivetel:
        print(f"Hiba! A Hallgato.hallgatok lista üres! Hiba üzenet: {lista_ures_kivetel}", file=sys.stderr)
        
    print(f"Legfiatalabb hallgató: {legfiatalabb}")
    print(f"Legidősebb hallgató: {legidosebb}")
    
    print("PTI-s hallgatók:")
    for hallgato in Hallgato.szak_hallgato("PTI"):
        print(f"{hallgato.nev} ", end="")
    print()

if __name__ == '__main__':
    main()