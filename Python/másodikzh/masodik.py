from webes_feladat import find_strongest_hero
from webes_feladat import find_hosok

#Windows: python -m pytest -v
#Linux: pytest -v

def test_find_strongest_hero():
    #Mi történik, ha üres a `hosok_listaja` lista?
    ures_hosok_listaja = []
    assert [] == find_strongest_hero(ures_hosok_listaja)
    
    #Mi történik egy elemes bemenetre?
    egy_hos = {'class': 'Monk', 'level': 24, 'name': 'Erevan'}
    egy_elemes_hosok_listaja = [egy_hos]
    assert egy_hos == find_strongest_hero(egy_elemes_hosok_listaja)
    
    #Mi történik két elemes bemenetre?
    masik_hos = {'class': 'Rogue', 'level': 38, 'name': 'Firion'}
    ket_elemes_hosok_listaja = [egy_hos, masik_hos]
    assert masik_hos == find_strongest_hero(ket_elemes_hosok_listaja)
    
    #Tényleg egy három kulcsos szótárat kapunk vissza?
    assert 3 == len(find_strongest_hero(egy_elemes_hosok_listaja).keys())

def test_find_hosok():
    #Hogyan viselkedik a függvény üres bemenetre?
    ures_hosok_nevei = []
    assert [] == find_hosok(ures_hosok_nevei)
    
    #Mi történik egy elemes bemenetre?
    hos_neve = "Erevan"
    egy_elemes_hos_nevei = [hos_neve]
    assert egy_elemes_hos_nevei == find_hosok(egy_elemes_hos_nevei)
    
    #Mi történik több elemes bemenetre?
    tobb_elemes_hos_nevei = ["Erevan", "Firion"]
    assert egy_elemes_hos_nevei == find_hosok(tobb_elemes_hos_nevei)