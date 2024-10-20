# Zählschleife

# Ausgabe auf Bildschirm
# 0 1 2 3 4 5

for i in range(6):
    print(i, end=' ')
# print() # 

# Mit Start und Endbedingung
for i in range(10, 31):
    print(i, end=' ')
print() # Um eine neue Zeile zu setzen

# Mit Start- und Endbedingung und Schrittweite
for i in range(2, 40, 2):
    print(i, end=' ')
print()

# Rückwärts
for i in range(40, 0, -2):
    print(i, end=' ')

# range(start_bed, end_bed, schrittweite)

# start ist immer inklusive (also enthalten)
# ende ist exklusive (also nicht enthalten)