

class Netcalc:

    def __init__(self, ipv4_dec, cidr):
        self.ipv4_dec = ipv4_dec
        self.cidr = cidr
        print("Ipv4:",ipv4_dec, "CIDR:",cidr)
        self.network_id = (0,0,0,0)
        self.netmask_decimal = (0,0,0,0)
        self.network_broadcast = (0,0,0,0)
        self.sum_hosts = 0
        self.usable_host_ips = [(0,0,0,0), (0,0,0,0)]

    def __find_network_id(self, ipv4_dec):
        #convert ipv4_dec to binary
        pass





#Test
netcalc = Netcalc((192,168,132,197), 24)