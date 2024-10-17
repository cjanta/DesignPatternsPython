import random

def lotto_spielen(eigene_zahlen, eigene_superzahl):

    while len(eigene_zahlen) < 6:
        zahl = int(input("Bitte gib eine Zahl zwischen 1 und 49 ein: "))
        if zahl not in eigene_zahlen and 1 <= zahl <= 49:
            eigene_zahlen.append(zahl)
        else:
            print("Zahl ungültig. Bitte gib eine andere Zahl ein.")

    while not 0 <= eigene_superzahl <= 9:
        temp_super = int(input("Bitte gib die Superzahl (0-9) ein: "))
        if  0 <= temp_super <= 9:
            eigene_superzahl = temp_super
        else:
            print("Superzahl ungültig. Bitte gib eine andere Zahl zwischen 1 und 49 ein.")
       
    print("Deine Gewinnkombination:", *eigene_zahlen," Superzahl: " ,eigene_superzahl)

    ziehungen = set()
    while len(ziehungen) < 6:
        ziehungen.add(random.randint(1, 49))
    ziehungen = sorted(list(ziehungen))
    superzahl = random.randint(0, 9)

    print("Ziehung beendet:", *ziehungen, " Superzahl: " , superzahl)

    if set(eigene_zahlen) == set(ziehungen) and eigene_superzahl == superzahl:
        print(f"\nGewonnen")
        print("Deine Gewinnkombination:", *eigene_zahlen, eigene_superzahl)
    elif (eigene_superzahl == superzahl):
        print("Höööy - feuchter Händedruck, die Superzahl ist richtig.")
    else:
        print("Leider verloren. Deine Looserkombination:",*eigene_zahlen, " Superzahl: " , eigene_superzahl)        

        

lotto_spielen([1,2,3,4,5,6],10)