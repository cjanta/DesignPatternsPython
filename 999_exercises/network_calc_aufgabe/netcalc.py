import ipaddress

class Netcalc:

    def __init__(self, ipv4_dec :str, cidr :str):
        self.ipv4_dec = ipv4_dec
        self.cidr = cidr
        print("Ipv4:",ipv4_dec, "CIDR:", cidr, int  )

        self.network = ipaddress.IPv4Network(ipv4_dec+ "/" + cidr, strict=False)
        self.__display_network()
        

    def __ipv4_to_binary(self, ipv4_dec):
        return '.'.join([f'{int(octet):08b}' for octet in str(ipv4_dec).split('.')])
    
    def __display_network(self):
        network_bin = self.__ipv4_to_binary(self.network.network_address)
        netmask_bin = self.__ipv4_to_binary(self.network.netmask)
        broadcast_bin = self.__ipv4_to_binary(self.network.broadcast_address)
        print(f"Network: {self.network.network_address} ({network_bin})")
        print(f"Netmask: {self.network.netmask} ({netmask_bin})")
        print(f"Broadcast address: {self.network.broadcast_address} ({broadcast_bin})")
        print(f"Number of hosts: {self.network.num_addresses - 2}")
        print(f"Usable hosts range: {list(self.network.hosts())[0]} - {list(self.network.hosts())[-1]}")


#Test
#netcalc = Netcalc("192.168.1.124", "24")

print("**************************************************************")

class BitMaster3000:
    #33bit
    max = 0b11111111111111111111111111111111
    min = 0b00000000000000000000000000000000

    def read_bit(num, position):
        # Shift 1 to the left by 'position' bits and use bitwise AND
        return (num >> position) & 1
    
    def set_bit(num, position):
        # Use bitwise OR to set the bit at 'position'
        return num | (1 << position)
    
    def clear_bit(num, position):
        # Use bitwise AND with the inverse (~) of the mask to clear the bit
        return num & ~(1 << position)
    
    def toggle_bit(num, position):
        # Use bitwise XOR to toggle the bit
        return num ^ (1 << position)



# Test readBit
# num = 0b101010  # 42 in decimal
# position = 2    # from left
# print(BitMaster3000.read_bit(num, position))  # Output: 1 (the 4th bit is 1)

#Test setBit, clearBit and toggleBit
num = BitMaster3000.max
  
# num = BitMaster3000.set_bit(num, 2)
# print(bin(num)) 

for i in range(0,32):
    num = BitMaster3000.clear_bit(num, i)
    #print(bin(num))  
    print(f"{num:32b}")

# num = BitMaster3000.toggle_bit(num, 31)
# print(bin(num)) 

