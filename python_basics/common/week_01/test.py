import random

a = "Hallo"
b = "Welt"
num = 2

# print(a,b, num)
# print(type(num))

# for i in range(10,100):
#         print(i)
# print()

# for i in range(2,41,2):
#         print(i)

random_number = -1
secret_number = 100
counter = 0

while (random_number != secret_number):
        random_number = random.randint(0, 101)
        counter += 1
# print("Nach " + str(counter) + " Versuchen wurde die Geheimnummer erreicht!")
print(f"Yay, {counter} Versuche")

# Schleife in Fussnote
while (True):
        random_number = random.randint(0, 101)
        if (random_number != secret_number):
                break