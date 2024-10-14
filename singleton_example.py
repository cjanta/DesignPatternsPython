class SingletonMeta(type):
    """
    Dies ist eine Metaklasse, die das Singleton-Designmuster implementiert.
    Sie stellt sicher, dass es nur eine Instanz der Singleton-Klasse gibt.
    """
    
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    """
    Beispiel einer Klasse, die das Singleton-Muster verwendet.
    """
    
    def __init__(self, value):
        self.value = value

# Beispielverwendung
singleton1 = Singleton("Erste Instanz")
singleton2 = Singleton("Zweite Instanz")

print(singleton1.value)  # Ausgabe: Erste Instanz
print(singleton2.value)  # Ausgabe: Erste Instanz
print(singleton1 is singleton2)  # Ausgabe: True
