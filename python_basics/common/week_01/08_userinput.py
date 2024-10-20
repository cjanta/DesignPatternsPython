# Eingabe für Anwendende ermöglichen


alter = 49

if (alter >= 18):
    "Du bist voll und jährig!"

# Durch Usereingaben wird es dynamisch

# 'eingabe' muss überprüft werden, ob ein Zahlwert enthalten ist
# erst wenn die Eingabe ein numeraler Wert ist, wird die
# Fallunterscheidung vorgenommen
eingabe = input("Wie alt bist Du: ") # Hallo


if (int(eingabe) >= 18):
    print("Du bist voll und jährig!")
else:
    print("Du bist zu jung")

print(eingabe)
