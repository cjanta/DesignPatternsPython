import doctest


def quadriere(zahl):
    """
    Quadriert die Zahl 'zahl' und gibt den Wert zurück
    
    >>> quadriere(2)
    4
    >>> quadriere(-3)
    9
    >>> quadriere(15)
    225
    """
    return zahl * zahl



# Direkt im Programmablauf testen
doctest.testmod()


# Terminal im Ordner dieser Datei öffnen
# python3 -m doctest <dateiname.py>