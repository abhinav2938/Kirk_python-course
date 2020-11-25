import requests
import os
import json
from pprint import pprint
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category = InsecureRequestWarning)

if __name__ == '__main__':
    
    token = os.environ['NETBOX_TOKEN']
    device_id = input('enter the device id of the created object: ')
    url = 'https://netbox.lasthop.io/api/ipam/ip-addresses/'
    #It's not always required to do a get first before put
#    http_headers = {}
#    http_headers['accept'] = 'application/json; version=2.4;'
#    http_headers["Authorization"] = f"Token {token}"
#
#    response = requests.get(url, headers = http_headers,  verify = False)
#    new_ip = response.json()

    #now doing PUT operation so different headers
    http_headers = {'Content-Type': 'application/json; version=2.4;',
        'Authorization' : 'Token {}'.format(token)
    }
    #now modify by adding a description
    data = {
            'address' : '1.1.1.1/32',
            'description' : 'Rest-API testing'
            }    

    response = requests.put(f'{url}{device_id}/', headers = http_headers, data = json.dumps(data), verify = False)
    
    print()
    #Note: to get the status code you don't need to use the json() function, if you do it will not work
    print(f'status code: {response.status_code}')
    print('#'*80)
    pprint(response.json())    



