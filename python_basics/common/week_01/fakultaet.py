# Fakultät in der Mathematik wird mit ! gekennzeichnet

# 5 Fakultät -> 5!
# 5 * 4 * 3 * 2 * 1

# Dazu bitte eine Methode definieren. Die Fakultät soll dabei Variabel

def faculty(value):
    if value < 1:
       return "Abbruch"
    fac = 1
    for number in range(value):
        fac *= (number + 1)
    return fac

print(faculty(-1))

# 49! / (43! + 6!)
