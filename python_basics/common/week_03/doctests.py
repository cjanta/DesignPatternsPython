import doctest



def quadriere(zahl):
    # Achtung, keine Leerzeichen am Ende der Zeilen sonst liest doctest die Tests falsch
    # Also keine leading und trailing spaces. Genau nur so schreiben wie folgt:
    # >>> quadriere(2)
    # 4
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