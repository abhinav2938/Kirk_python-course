import requests
import json
import os
from pprint import pprint

from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category= InsecureRequestWarning)


if __name__ == '__main__':

    #token = '63aa375e2590159ca3171c5269931043b85d33cf'
    token = os.environ['NETBOX_TOKEN']
    url = 'https://netbox.lasthop.io/api/dcim/devices/8/'
    #url = 'https://api.github.com/'
    http_headers = {'accept': 'application/json; version=2.4;',
            'authorization' : 'Token {}'.format(token),
        }
    response = requests.get(url, headers = http_headers, verify = False)
    arista10 = response.json()

    #Now doing PUT operation with new http_headers
    http_headers = {'Content-Type' : 'application/json; version=2.4;',
            'authorization' : 'Token {}'.format(token),
        }

    #Reformat to modify the arista10 object
    
    for field in ['device_role', 'device_type', 'platform' ,'site' , 'rack']:
        arista10[field] = arista10[field]['id']
    
    arista10['status'] = 1

    arista10['rack'] = 2

    response = requests.put(url, headers = http_headers, data = json.dumps(arista10), verify = False)
    response = response.json()
    
    print()
    pprint(response)
    print()
