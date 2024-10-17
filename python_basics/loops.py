

obstarten = ["Apfel", "Birne", "Traube", "Raspberry"]


# for obst in obstarten:
#     print(obst)

for i in range(0, len(obstarten)):
    print(i, obstarten[i])

for i, moff in enumerate(obstarten):
    if moff == "Raspberry":
        obstarten[i] = "Rubus Idaeus"
print(obstarten)