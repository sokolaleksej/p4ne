import re
import glob



def Classif (s):

    IP = re.match("^ ip address ([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+) ([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)", s)
    if IP:
        return ("IP", IP.group(1), IP.group(2))



n= glob.glob("d:\\Соколов\\Курс Python\\config_files\\*.txt")
for i in n:
  f = open(i,'r')
  lines = f.readlines()
  f.close()
  for j in lines:
        spisok = Classif(j)

        print (spisok)
