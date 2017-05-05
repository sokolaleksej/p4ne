import argparse
import requests
import pprint



parser = argparse.ArgumentParser()
parser.add_argument('card',nargs='*')
arg = parser.parse_args()



for i in arg.card:
    r = requests.get('https://lookup.binlist.net/'+i, headers = {'Accept-Version': '3'})
    pprint.pprint (r.json()['bank']['name'])
