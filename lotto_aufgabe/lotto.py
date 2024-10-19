import random
import pickle

def lotto_spielen(eigene_zahlen, eigene_superzahl):

    while len(eigene_zahlen) < 6:
        readEigeneZahlen(eigene_zahlen)    

    while len(eigene_superzahl) < 1:
        readEigeneSuperzahl(eigene_superzahl)    

    print("Gewinnchance gem: (49!/(43! + 6!)) * 10 beträgt:", calculate_chances_with_super()) 
    print("Deine gewählte Gewinnkombination:", *eigene_zahlen," Superzahl: " , eigene_superzahl)

    #lotto_geld = 1000 * 1000 * 1000 # 1mia
    #lotto_geld = 1000 * 1000 # 1mio
    lotto_geld = 1000 * 100
    lotto_ziehungen_count = 0
    #ziehungen_zu_anzahl = {} # Dictionary mit Tupel(1,2,3,4,5,6,7) zu 1..* zähler

    while(True):
        lotto_ziehungen_count += 1   
        gezogene_kugeln = ziehung_6_aus_49() 
        gezogene_super_kugel = ziehung_superzahl()
        #add_ziehung_to_dicitionary(ziehungen_zu_anzahl, gezogene_kugeln, gezogene_super_kugel)

        # Auswertung
        hits = treffer(eigene_zahlen,gezogene_kugeln)
        super_hit = super_treffer(eigene_superzahl, gezogene_super_kugel)
        wc = eval_winning_class(hits, super_hit)
        if wc > -1:
            print(f"Ziehung: {lotto_ziehungen_count} beendet:", *gezogene_kugeln, [gezogene_super_kugel], "Treffer:", hits, "Superzahl getroffen:", super_hit_to_print(super_hit) , wc_to_print(wc) )

        if do_we_have_winner(eigene_zahlen, gezogene_kugeln, eigene_superzahl, gezogene_super_kugel):
            print(f"\nWE HAVE A WINNER !!!11")
            print("Deine Gewinnkombination:", *eigene_zahlen, eigene_superzahl, f"nach {lotto_ziehungen_count} versuchen")
            break   
        elif (lotto_ziehungen_count >= lotto_geld):
            print(f"\nBankrott nach {lotto_ziehungen_count} Versuchen")
            print("Gewinnchance gem: (49!/(43! + 6!)) * 10 beträgt:", calculate_chances_with_super()) 
            print("Deine Looserkombination:", *eigene_zahlen, eigene_superzahl)
            break
    
    #save_ziehungen_zu_anzahl(ziehungen_zu_anzahl)

def add_ziehung_to_dicitionary(ziehungen_zu_anzahl, gezogene_kugeln, gezogene_super_kugel):
    dict_key = tuple(gezogene_kugeln) + tuple([gezogene_super_kugel])
    ziehungen_zu_anzahl[dict_key] = ziehungen_zu_anzahl.get(dict_key, 0) + 1

def super_treffer(eigene_superzahl, gezogene_super_kugel):
    return eigene_superzahl[0] == gezogene_super_kugel

def do_we_have_winner(eigene_zahlen, gezogene_kugeln, eigene_superzahl, super_kugel):
    return set(eigene_zahlen) == set(gezogene_kugeln) and super_treffer(eigene_superzahl, super_kugel)
#test: def do_we_have_winner(eigene_zahlen, kugeln, eigene_superzahl, super_kugel):
# print(do_we_have_winner([1,2,3,4,5,6],[1,2,3,4,5,6],[7],7)) # assert true
# print(do_we_have_winner([1,2,3,4,5,6],[1,2,3,4,5,6],[7],6)) # assert false
# print(do_we_have_winner([1,2,3,4,5,6],[10,20,37,40,15,16],[0],0)) # assert false
# print(do_we_have_winner([1,2,3,4,5,6],[10,20,37,40,15,16],[1],0)) # assert false
# print(do_we_have_winner([1,2,3,5,4,6],[2,1,3,4,6,5],[7],7)) # assert true

def treffer(eigene_zahlen, kugeln):
    return len([zahl for zahl in kugeln if zahl in eigene_zahlen])

def eval_winning_class(treffer, super_treffer):
    # 6 == wc 2
    # 5 == wc 4
    # 4 == wc 6
    # 3 == wc 8
    wc = ((6 - treffer) * 2) + 2
    if super_treffer:
         wc -= 1
    if wc > 9:
       return 0
    return wc

def print_ziehungen_zu_anzahl(ziehungen_zu_anzahl): 
    print("\nHäufigkeit der gezogenen Kombinationen (> 1):")
    for dict_key, value in ziehungen_zu_anzahl.items():
        if (value > 1):
            print(dict_key, "kam", value, "mal vor.")

def wc_to_print(wc):
    if wc > 0:
        return "Gewinnklasse: " + str(wc)
    return "Theo sagt Danke, viel Glück beim nächsten mal."



def super_hit_to_print(super_hit):
    if super_hit:
        return "JA"
    return " NEIN"

def save_ziehungen_zu_anzahl(ziehungen_zu_anzahl):
    with open('saved_ziehungen.pkl', 'wb') as f:
        pickle.dump(ziehungen_zu_anzahl, f) 

def load_ziehungen_zu_anzahl():
    with open('saved_ziehungen.pkl', 'rb') as f:
        return pickle.load(f)  

def faculty(it):
    fakultät = 1
    for i in range(1, it +1):
        fakultät = fakultät * i
    return fakultät

def calculate_chances_with_super():
    total_fac = faculty(49)
    r = faculty(43) + faculty(6)
    return (total_fac/r) * 10

def ziehung_superzahl():
    return random.randint(0, 9)

def ziehung_6_aus_49():
    kugeln = []
    for i in range(1,50):
        kugeln.append(i)
    
    gezogene_nummern = []
    for i in range(0,6):
        next = random.randint(0, len(kugeln)-1)     
        kugel = kugeln[next]
        kugeln.remove(kugel)
        gezogene_nummern.append(kugel)

    return gezogene_nummern

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




#TEST

lotto_spielen([1,2,3,4,5,6],[7]) 
#lotto_spielen([],[]) # mit userEingabe

#print_ziehungen(load_ziehungen())