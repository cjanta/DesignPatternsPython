import random

def lotto_spielen(eigene_zahlen, eigene_superzahl):

    while len(eigene_zahlen) < 6:
        readEigeneZahlen(eigene_zahlen)    

    while len(eigene_superzahl) < 1:
        readEigeneSuperzahl(eigene_superzahl)    

    print("Gewinnchance gem: (faculty(49)/(faculty(43) + faculty(6))) * 10: ", print_chances_with_super()) 
    print("Deine gewählte Gewinnkombination:", *eigene_zahlen," Superzahl: " , eigene_superzahl)

    #lotto_geld = 1000 * 1000 # 1mio
    lotto_geld = 1000 * 10 # 10 tausend
    lotto_ziehungen_count = 0
    ziehungen = {}
    while(True):
        lotto_ziehungen_count += 1   
        lotto_ziehung = ziehung_6_aus_49() 
        kugeln = lotto_ziehung[0]
        super_kugel = lotto_ziehung[1]
        dict_key = tuple(kugeln) + tuple([super_kugel])
        ziehungen[dict_key] = ziehungen.get(dict_key, 0) + 1
        print(f"Ziehung: {lotto_ziehungen_count} beendet:", *kugeln, " Superzahl: " , super_kugel)

        if do_we_have_winner(eigene_zahlen, kugeln, eigene_superzahl, super_kugel):
            print(f"\nGewonnen")
            print("Deine Gewinnkombination:", *eigene_zahlen, eigene_superzahl, f"nach {lotto_ziehungen_count} versuchen")
            break   
        elif (lotto_ziehungen_count >= lotto_geld):
            print(f"\nBankrott nach {lotto_ziehungen_count} Versuchen")
            print("Gewinnchance gem: (faculty(49)/(faculty(43) + faculty(6))) * 10: ", print_chances_with_super()) 
            print("Deine Looserkombination:", *eigene_zahlen, eigene_superzahl, f"nach {lotto_ziehungen_count} versuchen")
            break
    print_kombinationen(ziehungen)

def do_we_have_winner(eigene_zahlen, kugeln, eigene_superzahl, super_kugel):
    return set(eigene_zahlen) == set(kugeln) and eigene_superzahl == super_kugel

def print_kombinationen(ziehungen):
    print("\nHäufigkeit der gezogenen Kombinationen (> 1):")
    for dict_key, value in ziehungen.items():
        if (value > 1):
            print(dict_key, "kam", value, "mal vor.")

def faculty(it):
    fakultät = 1
    for i in range(1, it +1):
        fakultät = fakultät * i
    return fakultät

def print_chances_with_super():
    total_fac = faculty(49)
    r = faculty(43) + faculty(6)
    return (total_fac/r) * 10
    

def ziehung_6_aus_49():
    kugeln = set()
    while len(kugeln) < 6:
        kugeln.add(random.randint(1, 49))
    kugeln = sorted(list(kugeln))
    superzahl_kugel = random.randint(0, 9)
    return [kugeln, superzahl_kugel]

def readEigeneZahlen(eigene_zahlen):
    c = len(eigene_zahlen) + 1
    zahl = int(input(f"Bitte gib die {c}. Zahl zwischen 1 und 49 ein: "))
    if zahl not in eigene_zahlen and 1 <= zahl <= 49:
        eigene_zahlen.append(zahl)
    else:
        print("Zahl ungültig. Bitte gib eine andere Zahl ein.")

def readEigeneSuperzahl(eigene_superzahl):
    zahl = int(input("Bitte gib die Superzahl (0-9) ein: "))
    if  0 <= zahl <= 9:
        eigene_superzahl.append(zahl)
    else:
        print("Superzahl ungültig. Bitte gib eine andere Zahl (0-9) ein.")


#test der gewinner ermittlung
# print(do_we_have_winner([1,2,3,4,5,6],[1,2,3,4,5,6],[7],[7])) # true
# print(do_we_have_winner([1,2,3,4,5,6],[1,2,3,4,5,6],[7],[6])) # false
# print(do_we_have_winner([1,2,3,4,5,6],[1,2,37,4,5,6],[7],[6])) # false

lotto_spielen([1,2,3,4,5,6],[7])
#lotto_spielen([],[]) 