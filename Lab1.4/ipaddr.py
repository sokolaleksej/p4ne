import ipaddress
import random

class IPv4RandomNetwork(ipaddress.IPv4Network):
    def __init__(self):
        n = (random.randint(2**24,2**32-1))
        m = (random.randint(0, 32))
        ipaddress.IPv4Network.__init__(self, (n, m) ,strict=False)

list1=[]

for i in range(0,10):
    list1.append(IPv4RandomNetwork())




def sortfunc (ipnet):
    return int(ipnet.network_address._ip)+ int(ipnet.netmask._ip*2**32)
for i in sorted(list1, key=sortfunc):
    print (i)
