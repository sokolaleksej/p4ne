import requests, json, pprint
from flask import Flask, jsonify, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('topology.html')


@app.route('/api/topology')
def web():
    return jsonify (requests.get(url2, headers=header, verify=False).json()['response'])



def new_ticket():
    url = 'https://sandboxapic.cisco.com/api/v1/ticket'
    payload = {"username": "devnetuser",
               "password": "Cisco123!"}
    header = {"content-type": "application/json"}
    response = requests.post(url, data=json.dumps(payload),
                             headers=header, verify=False)
    return response.json()['response']['serviceTicket']



if __name__ == '__main__':
    ticket = new_ticket()
    controller = "devnetapi.cisco.com/sandbox/apic_em"
#    url = "https://" + controller + "/api/v1/host"
#    url1 = "https://" + controller + "/api/v1/network-device"
    url2 = "https://" + controller + "/api/v1/topology/physical-topology"

    header = {"content-type": "application/json",
              "X-Auth-Token": ticket}

#    responce = requests.get(url, headers=header, verify=False)
#    print("Hosts = ")
#    pprint.pprint(json.dumps(responce.json()))

#    responce = requests.get(url1, headers=header, verify=False)
#    print("Network-device = ")
#    pprint.pprint(json.dumps(responce.json()))

#    responce = requests.get(url2, headers=header, verify=False)
#    print("Topology = ")
#    pprint.pprint(json.dumps(responce.json()))

app.run(debug=True)