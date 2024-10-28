# Abschlussprüfung "Die Zeitreise"
Viel Spaß! Und daran denken, AI (Künstliche Intelligenz) ist nicht erlaubt! 


# 1. Aufgabe (+7 Motivation / +7 Erfolgserlebnis)
## **Aufgabenstellung zu a**
````
Noch immer gibt es Menschen, die den Euro in DM umrechnen.   
Um diese Menschen zu unterstützen, erstellen Sie eine  
Methode dafür.   
Diese Methode nimmt einen Euro-Wert entgegen und gibt den Wert in DM aus.  
Und nur das. Das ist das Minimal Valuable Product (MVP).  
````
## **Teilaufgabe a**
````
Erstellen sie eine Methode, die den umgerechneten Betrag, unter Angabe des Währungszeichens, ausgibt.  
Das Ergebnis ist auf 2 Nachkommastellen kaufmännisch zu runden.  
Variablen-, wie auch Methodennamen, müssen sinnvoll gewählt werden.   
(Sollten Sie den Umrechnungskurs für Euro in DM nicht kennen, so nehmen Sie bitte an,  
dass 1.955,83 DM einem Betrag von 1.000,00 € entsprechen)  
````
## **Lösung a**  
```py
def round_to_two_digits(float_in_str : str):
    value = float(float_in_str) * 100 
    if value > 0:
        rounded_value = int(value + 0.5)
    else:
        rounded_value = int(value - 0.5)
    return rounded_value / 100

def convert(euro : str):
    print("€",round_to_two_digits(euro))
    dm_to_1k_euro = 1955.83
    result = dm_to_1k_euro * float(euro) / 1000
    return str(round_to_two_digits(result)) + ' DM'


print(convert(107))
```

## **Aufgabenstellung zu b**
````
Prima, stellen Sie fest, das klappt super, als das Telefon klingelt.  
Camelia Höcker ist an der anderen Seite zu hören.  
Sie beklagt sich, dass das Programm abgestützt sei, wegen Ihrer fehlerhaften Erweiterung.  
Sie habe alles richtig gemacht.  
Sie gibt ‚1.337,73 EUR‘ ein, klickt auf „Umrechnen“ und dann geht nichts mehr.  
Natürlich erkennen Sie das Problem sofort. Sie entschuldigen sich,  
dass Ihre Anwendung gegen Layer-8-Attacken nicht gehärtet sei und versprechen Ihr,  
dass Sie sich gleich darum kümmern werden.  
Zunächst sagen Sie Ihr, was den Absturz bewirkt, und nennen Ihr einen  
Workaround, bis Sie das Update erstellt haben und der ValueError abgefangen wird.  
````
## **Teilaufgabe b**
````  
Wie kann Frau Höcker bis zum Update mit Ihrer Methode arbeiten,
ohne dass es zu Abbrüchen kommt?
````
## **Lösung zu b**  
Den Euro Betrag sollte sie genau nur in folgendem format angeben 111.11
Die Ganzen Zahlen ohne Sonderzeichen in einer reihe, dann anstelle des Kommas einen Punkt setzten und genau nur 2 Nachommastellen angeben ohne weitere Sonderzeichen.

## **Teilaufgabe c**
````  
Die Kundin fragt, wie Sie das lösen wollen.
Gerne erklären Sie, wie Sie diesen Fehler behandeln können
und was dazu notwendig ist
````
## **Lösung zu c**  
Die Eingabeüberprüfung muss erweitert werden um gebräuchliche eingabe formate zu unterstützen.
1. Die gebräuchliche Notation, die Tausender Stellen  
 durch einen "." zu markieren muss erkannt und   
 eine rohe Ganzzahl, durch entfernen der "." Zeichen, erstellt werden.  
2. Das in der EU gebräuchliche "Komma"   
    zur Abtrennung des Dezimalteils   
    muss erkannt und durch einen "." ersetzt werden  

## **Teilaufgabe d**
````  
Erweitern Sie Ihre Applikation so, wie Sie es beschrieben haben:
````
## **Lösung zu d**  
````py

def round_to_two_digits(float_in_str : str):
    value = float(float_in_str) * 100 
    if value > 0:
        rounded_value = int(value + 0.5)
    else:
        rounded_value = int(value - 0.5)
    return rounded_value / 100

def is_float(input :str):
    try:
        float(input)
        return True
    except ValueError:
        return False
    
def is_number(value :str):
        for char in value:
            #print("Zeichen", char, "ASCII", ord(char))
            if (ord(char) < 48) or (ord(char) > 57):
                #print(value, "ist keine Nummer!")
                return False
        #print(value, "ist eine Nummer!")
        return True 
    
def check_custom_formats(input :str):
    count_p = 0
    count_c = 0
    index_c = 0

    for i in range(0, len(input)):
        if input[i] == '.':
            count_p += 1
        elif input[i] == ',':
            index_c = i
            count_c += 1
    
    if count_c == 1:
       input = input.replace(',', '.')
    elif count_c > 1:
        raise Exception("Eingabeformat: " + input + " wird leider nicht unterstützt.")
    
    if is_float(input):
        return input

    #print("needed formatting")
    formated_input = ""
    for i in range(0, len(input)):
        if is_number(input[i]) or i == index_c:
            formated_input += input[i]


    return formated_input   
#print(check_custom_formats("1.000.000,0"))
    
def convert(euro_string : str):
    if not is_float(euro_string):
        euro_string = check_custom_formats(euro_string)
    
    print("€",round_to_two_digits(euro_string))
    dm_to_1k_euro = 1955.83
    result = dm_to_1k_euro * float(euro_string) / 1000
    return str(round_to_two_digits(result)) + ' DM'

#input_string = input("Bitte einen Betrag in € angeben um diesen in DM umrechnen zu lassen:")
#input_string = "1.000.000,569" #expected: 1000000,57
input_string = '100,7777' #expected: 100,78
print(convert(input_string))
````

## **Teilaufgabe e**
````  
Wie könnte eine Methode auch die Eingabe Frau Höckers verarbeiten,
so dass der Betrag und die Währungseinheit erkannt werden.
Die Methode gibt ein tuple() mit dem Betrag und der Währungseinheit zurück
````
## **Lösung zu e**  
````py

def round_to_two_digits(float_in_str : str):
    value = float(float_in_str) * 100 
    if value > 0:
        rounded_value = int(value + 0.5)
    else:
        rounded_value = int(value - 0.5)
    return rounded_value / 100

def is_float(input :str):
    try:
        float(input)
        return True
    except ValueError:
        return False
    
def is_number(value :str):
        for char in value:
            #print("Zeichen", char, "ASCII", ord(char))
            if (ord(char) < 48) or (ord(char) > 57):
                #print(value, "ist keine Nummer!")
                return False
        #print(value, "ist eine Nummer!")
        return True 
    
def check_custom_formats(input :str):
    count_p = 0
    count_c = 0
    index_c = 0

    for i in range(0, len(input)):
        if input[i] == '.':
            count_p += 1
        elif input[i] == ',':
            index_c = i
            count_c += 1
    
    if count_c == 1:
       input = input.replace(',', '.')
    elif count_c > 1:
        raise Exception("Eingabeformat: " + input + " wird leider nicht unterstützt.")
    
    if is_float(input):
        return input

    #print("needed formatting")
    formated_input = ""
    for i in range(0, len(input)):
        if is_number(input[i]) or i == index_c:
            formated_input += input[i]
    return formated_input   
    
def convert_euro_dm(euro_string : str):
    if not is_float(euro_string):
        euro_string = check_custom_formats(euro_string)
    
    print("€",round_to_two_digits(euro_string))
    dm_to_1k_euro = 1955.83
    result = dm_to_1k_euro * float(euro_string) / 1000
    return str(round_to_two_digits(result))

def convert_dm_euro(dm_string : str):
    if not is_float(dm_string):
        dm_string = check_custom_formats(dm_string)
    
    print("DM",round_to_two_digits(dm_string))
    dm_to_1k_euro = 1955.83
    result =  float(dm_string) * (dm_to_1k_euro / 1000) 
    return str(round_to_two_digits(result)) 

def convert(currency_string :str):
    if currency_string.__contains__("EU"):
        return convert_euro_dm(currency_string) , "DM"
    elif currency_string.__contains__("DM"):
        return convert_dm_euro(currency_string), "€"

#input_string = input("Bitte einen Betrag in € angeben um diesen in DM umrechnen zu lassen:")
#input_string = "1.000.000,569" #expected: 1000000,57
input_string = '100,7777 EU' 
input_string = '100,00 DM'
print(convert(input_string))
````

## **Teilaufgabe f**
````  
Erweitern Sie Ihre Anwendung so, dass Eingaben der Form‚
420,73 DM‘ in Euro und ‚71383,733 EUR‘ in DM umgerechnet
und ausgegeben werden. 
Nutzen Sie dazu gerne die Methoden, die Sie in den Aufgaben zuvor erstellt haben.
````
## **Lösung zu f**  
siehe Lösung e

## **Teilaufgabe g**
````  
Ermöglichen Sie auch die Anwendung auf Konsolenebene mit Parameterübergabe.
Nehmen Sie hierzu an, dass Ihre Datei ‚converter.py‘ heißt. 
Wird auf Konsolenebene‚ python converter.py „5 DM“‘ eingegeben,
so muss als Ausgabe auf der Kommandozeile der umgerechnete Betrag in Euro ausgegeben werden.
(Der Import, der zum Abfangen der Argumente benötigt wird, ist selbstredend erlaubt)
````
## **Lösung zu g: Finale converter.py**  
````py
import sys

def round_to_two_digits(float_in_str : str):
    value = float(float_in_str) * 100 
    if value > 0:
        rounded_value = int(value + 0.5)
    else:
        rounded_value = int(value - 0.5)
    return rounded_value / 100

def is_float(input :str):
    try:
        float(input)
        return True
    except ValueError:
        return False
    
def is_number(value :str):
        for char in value:
            #print("Zeichen", char, "ASCII", ord(char))
            if (ord(char) < 48) or (ord(char) > 57):
                #print(value, "ist keine Nummer!")
                return False
        #print(value, "ist eine Nummer!")
        return True 
    
def check_custom_formats(input :str):
    count_p = 0
    count_c = 0
    index_c = 0

    for i in range(0, len(input)):
        if input[i] == '.':
            count_p += 1
        elif input[i] == ',':
            index_c = i
            count_c += 1
    
    if count_c == 1:
       input = input.replace(',', '.')
    elif count_c > 1:
        raise Exception("Eingabeformat: " + input + " wird leider nicht unterstützt.")
    
    if is_float(input):
        return input

    #print("needed formatting")
    formated_input = ""
    for i in range(0, len(input)):
        if is_number(input[i]) or i == index_c:
            formated_input += input[i]
    return formated_input   
    
def convert_euro_dm(euro_string : str):
    if not is_float(euro_string):
        euro_string = check_custom_formats(euro_string)
    
    print("€",round_to_two_digits(euro_string))
    dm_to_1k_euro = 1955.83
    result = dm_to_1k_euro * float(euro_string) / 1000
    return str(round_to_two_digits(result))

def convert_dm_euro(dm_string : str):
    if not is_float(dm_string):
        dm_string = check_custom_formats(dm_string)
    
    print("DM",round_to_two_digits(dm_string))
    dm_to_1k_euro = 1955.83
    result =  float(dm_string) * (dm_to_1k_euro / 1000) 
    return str(round_to_two_digits(result)) 

def convert(currency_string :str):
    if currency_string.__contains__("EU"):
        return convert_euro_dm(currency_string) , "DM"
    elif currency_string.__contains__("DM"):
        return convert_dm_euro(currency_string), "€"

# TEST
if len(sys.argv) == 3:
    print(convert(sys.argv[1]+sys.argv[2]))
elif len(sys.argv) == 2:
    print(convert(sys.argv[1]+"EU"))
else:
    print(convert(input("Bitte einen Betrag und eine Währung ('EU' oder 'DM' oder '' für default 'EU') angeben um diesen umrechnen zu lassen.\n[>>>] ")))
````

# IF you're here you're there :)