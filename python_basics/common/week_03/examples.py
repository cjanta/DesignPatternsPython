
eine_Liste = [12, 45, 43 ,73 ,17 ,14, 12]

bit_list = [1,1,1,1,0,0,0,0]


# filter , map, sum

mapped_list = list(map(lambda v: v ^ 1, bit_list))
print("mapped_list",mapped_list)

# Was passiert mit dem Wert 240'?
print("240 ^ 0xff",240 ^ 0xff, "bin", bin(15))
#1111 0000
print("bin 240 ^ 0xff", bin(240 ^ 0xff))