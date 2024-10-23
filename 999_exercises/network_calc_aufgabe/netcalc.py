import ipaddress

class Netcalc:

    def __init__(self, ipv4_dec :str, cidr :str):
        self.ipv4_dec = ipv4_dec
        self.cidr = cidr
        print("Ipv4:",ipv4_dec, "CIDR:",cidr)
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
netcalc = Netcalc("192.168.1.124", "24")
