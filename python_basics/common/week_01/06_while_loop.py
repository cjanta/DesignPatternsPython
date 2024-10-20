import random

# while wird immer dann angewandt, wenn die Abbruchbedingung nicht
# eindeutig abzählbar ist

rnd_zahl = -1
secret_number = 100
counter = 0

while (rnd_zahl != secret_number):
    rnd_zahl = random.randint(0, 101)
    counter += 1
    print(counter)

print("Yay, erreicht! In", counter, 'Versuchen')


# Die Fußgesteuerte
# Gibt es nicht in Python
# Wird erreicht durch:

while (True):
    rnd_zahl = random.randint(1, 100)
    if (rnd_zahl == 100):
        break
print('Break wurde erreicht da rnd_zahl =', rnd_zahl)

# Java Pendant

# rnd_zahl = -1
# do {
#    rnd_zahl = int(Math.random() * 100 + 1);
# } while (rnd_zahl != 100);
