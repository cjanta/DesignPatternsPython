# Listen funktionieren wie die ArrayList in Java

liste = ['Äpfel', 'Birnen', 'Tomaten']

print (liste)

print (liste[1]) # Birnen

print('For-Each-Konstrukt')
# for-each
for i in liste:
    print(i)

print()
# Latürnich auch mit Zahlen

liste = [12, 45, 89, 4]
print("Liste mit Zahlwerten")
for i in liste:
    print (i)

print("\nAddition der Werte")
summe = 0
for i in liste:
    summe += i
print(summe)
