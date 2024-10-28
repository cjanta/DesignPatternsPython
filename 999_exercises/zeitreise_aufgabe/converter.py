
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