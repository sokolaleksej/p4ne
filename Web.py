from flask import Flask, jsonify
import sys
import re
import pprint
import glob

host = []
host1 = []
spisok1 = []

app = Flask(__name__)

@app.route('/')
@app.route('/index')

def index():
    return "Справка"

@app.route('/python')
def python():
    return jsonify(repr(sys.__dict__))

@app.route ('/configs')
def host():
    for j in spisok1:
        host = j.find('HOST')
        if host == 0: host1.append(j)
    return jsonify(host1)







if __name__ == '__main__':
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

    app.run(debug=True)

#for t in sorted(set(spisok1)):
#    print (t)
