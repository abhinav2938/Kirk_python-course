import requests
import os
import json
from pprint import pprint
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category = InsecureRequestWarning)

if __name__ == '__main__':
    
    token = os.environ['NETBOX_TOKEN']
    url = 'https://netbox.lasthop.io/api/ipam/ip-addresses/'
    http_headers = {}
    http_headers['Content-Type'] = 'application/json; version=2.4;'
    http_headers["Authorization"] = f"Token {token}"

    post_data = {
        "address": "192.0.2.100/32",
        }

    response = requests.post(url, headers = http_headers, data = json.dumps(post_data), verify = False)
    response = response.json()

    print()
    pprint(response)
