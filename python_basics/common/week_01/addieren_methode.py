# Methoden Funktionen Prozeduren

def addiere(zahl_1, zahl_2):
    return zahl_1 + zahl_2

print(addiere(5, 7))


# Addieren von Listenwerten

def summe_liste(liste):
    summe = 0
    for zahl in liste:
        summe += zahl
    return summe

zahlen = [23, 42, 187, 420, 17]
summe = summe_liste(zahlen)
print (summe)

# Geht auch so
print(summe_liste([23, 42, 187, 420, 17]))
