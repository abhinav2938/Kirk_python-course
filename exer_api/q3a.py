from pprint import pprint
import requests
import os

from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category = InsecureRequestWarning)

if __name__ == '__main__':
    url = 'https://netbox.lasthop.io/api/dcim/devices/'
    token = os.environ['NETBOX_TOKEN']
    http_headers = {}
    http_headers['accept'] = 'application/json; version = 2.4;'
    http_headers['authorization'] = f'Token {token}'

    response = requests.get(url,headers = http_headers, verify = False)

    print()
    result = response.json()['results']
    print('#'*80)
    for i in result:
        print(i['display_name'])   
 
    print()
