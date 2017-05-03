import re
import glob
import ipaddress


spisok1 = []
IP1 = []
gw = []

def Classif (s):

    IP = re.match("^ ip address ([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+) ([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)", s)
    if IP:
        return IP1.append((ipaddress.IPv4Network((IP.group(1), IP.group(2)), strict=False)))

    Gate = re.match('ip default-gateway (.*)', s)
    if Gate:
        return gw.append(ipaddress.IPv4Address(Gate.group(1)))




n= glob.glob("d:\\Соколов\\Курс Python\\config_files\\*.txt")
for i in n:
  f = open(i,'r')
  lines = f.readlines()
  f.close()
  for j in lines:
        Classif(j)


for t in (set(IP1)):
    print (t)
for r in (set(gw)):
    print (r)
#        spisok1.append(spisok)
#        spisok1 = ' '.join('spisok')

#print (set(spisok1))


#for t in (set(spisok1)):
#    print (t)
