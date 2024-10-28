from random import randint


class Zahlenratespiel():

    def __init__(self, start=1, ende=100):
        self.start = start
        self.ende = ende
        self.gemerkte_nummer = randint(start,ende)

    def is_not_a_number(self, value):
        try:
            int(value)
            return False
        except Exception as e:
            print(e)
            return True
        
    def is_nan_classic(self, value):
        # value muss zeichenweise iteriert werden
        for char in value:
            print("Zeichen", char, "ASCII", ord(char))
            if (ord(char) < 48) or (ord(char) > 57):
                print(value, "ist keine Nummer!")
                return True
        print(value, "ist eine Nummer!")
        return False 

    def mein_tipp(self, tipp):
        if tipp is None or tipp == '':
            raise Exception("Tipp ist leer oder None.\nDasProgramm wird beendet.")

        if tipp < self.start or tipp > self.ende:
            raise Exception(f"Der Tipp muss zwischen inklusive {self.start} und inklusive {self.ende} liegen\nDas Programm wird beendet.")

        if tipp < self.gemerkte_nummer:
            return 1
        elif tipp > self.gemerkte_nummer:
            return -1
        return 0
game = Zahlenratespiel()   
game.is_nan_classic("!")