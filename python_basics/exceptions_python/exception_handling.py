import random

def baue_den_turm_auf():
    if not random.randint(0,1):
        raise Exception("Turm fällt")
    print("turm aufgebaut")

for _ in range(10):
    try:
        baue_den_turm_auf()
    except Exception as e:
        print("Turm zusammengefallen")