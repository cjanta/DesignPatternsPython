
# Datei einlesen

datei_objekt = open("python_basics/FileIO/res/liste.csv", encoding="utf-8")
print(datei_objekt)
zeilen = datei_objekt.readlines()

for zeile in zeilen:
    print(zeile)