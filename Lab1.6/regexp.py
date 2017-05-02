import re
import glob

spisok1 = []

def Classif (s):

    IP = re.match("^ ip address ([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+) ([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)", s)
    if IP:
        return ("IP", IP.group(1), IP.group(2))

    INT = re.match("^interface (.+)", s)
    if INT:
        return ("INT", INT.group(1))

    HOST = re.match("^hostname (.+)", s)
    if HOST:
        return ("HOST", HOST.group(1))

    return ("UNCLASSIFIED",)

n= glob.glob("d:\\Соколов\\Курс Python\\config_files\\*.txt")
for i in n:
  f = open(i,'r')
  lines = f.readlines()
  f.close()
  for j in lines:
        spisok = ' '.join(Classif(j))
        if spisok != "UNCLASSIFIED":
            spisok1.append(spisok)


for t in sorted(set(spisok1)):
    print (t)


