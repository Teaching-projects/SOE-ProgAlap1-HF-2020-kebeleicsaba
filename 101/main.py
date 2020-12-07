from typing import Dict, List

Tippek=List[str]
"""Leadott tippek, azaz betűk listájának típusa."""

def kozte_van(betu:str, betuk:Tippek) -> bool:
    """Megadja, hogy a listában már benne van-e a megadott betű, vagy sem.

    Args:
        betu (str): a keresett betű
        betuk (Tippek): betűk listája

    Returns:
        bool: `True` ha benne van, `False` ha nincsen.
    """
    for i in betuk:
        if i == betu: return True
    return False

specialis_karakterek=[' ','.',',','!','?',':','-']

def megjelenites(szo:str, betuk:Tippek) -> str:
    """Visszaad egy olyan szót, amiben a `betuk`-ben lévő betűk látszanak, minden más helyére `_` kerül, kivéve 
    néhány speciális karaktert, amik megjelennek változtatás nélkül. Ezen karakterek listája a `specialis_karakterek` 
    globális listában adott.

    Kis és nagy betűket megkülönbözteti a függvény.

    Args:
        szo (str): a szó, aminek megjelenített változatát meg szeretnénk kapni. 
        betuk (Tippek): Egy karakterből, betűkből álló lista, amit már tippeltünk

    Returns:
        str: a megjelenített változata a szónak
    """
    visszateres = ''

    for i in szo:
        eppeniBetuJoe = False
        specko = False
        if kozte_van(i, betuk): eppeniBetuJoe = True
        if kozte_van(i, specialis_karakterek): specko = True
        if eppeniBetuJoe or specko: visszateres += i
        else: visszateres += "_"
    return visszateres


def megfejtett(szo:str, betuk:Tippek) -> bool:
    """Megadja, hogy sikerült-e már megfejtenünk a szót, azaz minden benne levő betű már a tippjeink között van.

    Args:
        szo (str): a kitalálandó szó
        betuk (Tippek): az eddig tippelt betűk

    Returns:
        bool: `True` ha teljesen megfejtettük a szót, `False` különben
    """
    """
    for tippBetu in betuk:
        if tartalmazza(szo, tippBetu) == False: return False
    return True
     """
    
    for i in szo:
        if kozte_van(i, betuk) == False: return False
    return True  

def tartalmazza(szo:str, betu:str) -> bool:
    """Megadja, hogy a megaadott betű szerepel-e a megadott szóban.

    Args:
        szo (str): a szó
        betu (str): a betű, amit keresünk, feltételezhető, hogy 1 karakter hosszú

    Returns:
        bool: `True` ha szerepel, `False` ha nem    
    """
    for i in szo:
        if betu == i: return True
    return False

def rossz_tippek(szo:str, betuk:Tippek) -> int:
    """Megadja, hogy hány rossz betűt tippeltünk eddig.

    Args:
        szo (str): a kitalálandó szó
        betuk (Tippek): az eddigi betű tippjeink

    Returns:
        int: a rossz tippek száma
    """
    rosszDb = 0
    """
    for i in szo:
        rossze = True
        for j in betuk:
            if j == i: rossze = False
        if rossze: rosszDb += 1
        """
    for i in betuk:
        rossze = True
        for j in szo:
            if j == i: rossze = False
        if rossze: rosszDb += 1

    return rosszDb 

def eletek(osszes:int,elhasznalt:int)->str:
    """Visszaad egy olyan szöveget, ami egy indikátor arra, hány életünk van még.

    A szöveg elején van annyi 😄 ahány életünk még maradt, majd annyi 💀 ahányat már "eljátszottunk".

    Args:
        osszes (int): az összes életünk száma
        elhasznalt (int): az eljátszott életek (rossz betű tippek) száma

    Returns:
        str: 😄😄😄💀💀 formátumú indikátor (a példa adatai: 5 összes, 2 elhasznált)
    """
    visszater = ''
    mosolygosDb = osszes - elhasznalt
    for i in range(osszes):
        if mosolygosDb > 0:
            visszater += '😄'
            mosolygosDb -= 1
        else: visszater += '💀'

    return visszater


def akasztofa(szo:str,osszes_elet:int) -> None:
    """Végigvisz egy akasztófa játékot, ahol a megadott szót kell kitalálni, és `osszes_elet` rossz tipp után vesztettünk.

    A játék minden körben először írja ki, hogy mit látunk a megfejtendő szóból, alá egy indikátort arról, hogy hány életünk van még,
    majd végül a tippelt karakterek listáját a tippek sorrendjében.

    Ezt követően az "Adja meg a kovetkezo betut: " kiírással kérjünk be egy betűt.
    Ellenőrzés nem szükséges se arra, hogy egyetlen betűt adtunk-e meg, se arra, hogy volt-e már korábban ez a betű.
    A megadott betűt irassuk is rögtön ki. (Szimplán, egymagában. Ennek pusztán annyi célja van, 
    hogy nyomon követhetőbbek legyenek az out fájlok.)

    Más kiiratás nem történik, a játék logikája egyértelmű: 
    addig adunk le tippeket betűkre, amíg vagy meg nem fejtődik a szó, vagy el nem fogynak az életeink.
    Többször leadhatjuk ugyanazt a tippet, de ez rossz, akkor több életet is vesz el.
    A kiíratott listában is jelenjen meg duplán akkor ez a betű.

    Ha nyertünk, még kerüljön kiírásra a megfejtett szó, valamint alá egy olyan szöveg, 
    hogy "Gratulalok, nyertel, es meg X eleted maradt!", ahol X értelemszerűen a megmaradt életek száma.

    Ha vesztettünk, akkor egy "Sajnalom, nem nyertel, ez lett volna a megoldas: MEGOLDAS".

    Példakimenetek adottak.
    

    Args:
        szo (str): a megfejtendő szó
        osszes_elet (int): az életeink száma, azaz hány rossz tipp után vesztettünk
    """
    kor = osszes_elet
    tippek = []
    nyertunk = False
    while kor > 0:
        print(megjelenites(szo, tippek))
        print(eletek(osszes_elet, rossz_tippek(szo, tippek)))
        print(tippek)
        betu = str(input("Adja meg a kovetkezo betut: "))
        print(betu)
        tippek.append(betu)
        if megfejtett(szo, tippek):
            nyertunk = True
            break
        
        if tartalmazza(szo, betu) == False: kor -= 1

    if nyertunk: 
        print(szo)
        print("Gratulalok, nyertel, es meg {} eleted maradt!".format(kor))


# Ez alatt ne tessek modositani.

szo=input()
maxelet=int(input())
akasztofa(szo,maxelet)





