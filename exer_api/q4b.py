import requests
import os
import json
from pprint import pprint
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category = InsecureRequestWarning)

if __name__ == '__main__':
    
    token = os.environ['NETBOX_TOKEN']
    
    url = 'https://netbox.lasthop.io/api/ipam/ip-addresses/240/'
    http_headers = {}
    http_headers['accept'] = 'application/json; version=2.4;'
    http_headers["Authorization"] = f"Token {token}"


    response = requests.get(url, headers = http_headers,  verify = False)
    response = response.json()

    print()
    pprint(response)
