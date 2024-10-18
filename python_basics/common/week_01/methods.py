

def addiere(z1, z2):
    return z1 + z2

print(addiere(5,5))

def addiere_Liste(liste):
    summe = 0
    for zahl in liste:
        summe += zahl
    return summe

print(addiere_Liste([1,2,3,4]))

#  5!

def fac(it):
    fakultät = 1
    for i in range(1, it +1):
        fakultät = fakultät * i
    return fakultät

print ("Fakultät: "  + str(fac(5)))

# Lotto 49! / (43! + 6!)

lotto = fac(49)
r = fac(43) + fac(6)
result = lotto/r
print(result) #10 068 347 520.0