import glob

spisok1 = []
glob.glob("d:\\Seafile\\p4ne_training\\config_files\\*.txt")

n= glob.glob("d:\\Seafile\\p4ne_training\\config_files\\*.txt")
for i in n:
  f = open(i,'r')
  lines = f.readlines()
  for j in lines:
        spisok = j.find('ip address')

        if spisok > 0: spisok1.append(j)

No_dup = list(set(spisok1))

for no_ip in No_dup:
    no_ip1 = no_ip.replace('ip address',' ').strip()

    print (no_ip1)


