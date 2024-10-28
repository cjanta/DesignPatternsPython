# Subnetting ipv4 qnd edit - Without using imports
# Daniel Kramer - dk@bellmann-engineering.com - 2024

def s(cidr) -> int:  # subnet
    return ((1 << cidr) - 1) << (32 - cidr)


def od(pos, ip_dec) -> int:  # octett as decimal value
    return ip_dec >> ((3 - pos) * 8) & 0xff


def ip_dec(ip: str) -> int:  # ip as 32 bit decimal value
    return sum(map(lambda x: x[1] << ((3 - x[0]) << 3), enumerate(map(int, ip.split('.')))))


def d(ip_dec) -> str:  # dotted decimal notation
    return f"{od(0, ip_dec)}.{od(1, ip_dec)}.{od(2, ip_dec)}.{od(3, ip_dec)}"


def calc_subnet(ip: str, cidr: int) -> tuple:
    i, c, ci = ip_dec(ip), s(cidr), (s(cidr) ^ 0xffffffff)
    return 2 ** (32 - cidr), 2 ** (32 - cidr) - 2, d(i & c), d((i & c) + 1), d((i | ci) - 1), d((i | ci))


# calc_subnet returns a tuple
# <num addresses, num clients, net id, first client's ip address, last client's ip address, broadcast address>
print(calc_subnet('192.168.1.42', 30))
print(calc_subnet('10.147.219.31', 12))

# TODO: MEMO an mich selbst: Versuchen einmal, im Detail, nachzuvollziehen
