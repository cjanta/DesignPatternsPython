# For-Each Schleife

obstarten = ['Apfel', 'Birne', 'Traube', 'Raspberry', 'Dingleberry']


# Iterieren über die Liste obstarten
for obst in obstarten:
    print(obst)

# Wie kann ich den Index ermitteln
for i in range(len(obstarten)):
    print(i, obstarten[i])

# for-each mit enumerate.
for index, value in enumerate(obstarten):
    if value == 'Dingleberry':
        obstarten[index] = 'Klabusterbeere heißt das'
    
print (obstarten)
