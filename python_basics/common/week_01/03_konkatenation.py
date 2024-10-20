# Python ist nicht streng typisiert

a = 'Hallo'

b = 'Welt'

print (a + b) # Output: HalloWelt
print (a + ' ' + b) # Output: Hallo Welt

print (a, b)  # Output: Hallo Welt

num = 2

# Ausgabe soll sein: Hallo Welt 2

print (a + ' ' + b + ' ' + str(num)) # Output: Hallo Welt 2

#oder auch

print(a, b, num)
