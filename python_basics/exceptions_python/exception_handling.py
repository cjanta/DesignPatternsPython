import random

class TowerCollapsException(Exception):
    def __init__(self, message):
        super().__init__(message)

def baue_den_turm_auf():
    if not random.randint(0,1):
        raise TowerCollapsException("Turm fällt")
    print("turm aufgebaut")

for _ in range(10):
    try:
        baue_den_turm_auf()
    except Exception as e:
        print( str(e) + "Turm zusammengefallen: ")

