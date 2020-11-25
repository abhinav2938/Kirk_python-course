import requests
from pprint import pprint
import os

from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category = InsecureRequestWarning)

def main():

    token = os.environ['NETBOX_TOKEN']
    url = 'https://netbox.lasthop.io/api/ipam/ip-addresses/'
    device_id = input('enter device id to be deleted: ')    

    http_headers = {
    'Content-type': 'application/json; version=2.4;',
    'Authorization' : 'Token {}'.format(token)
    }
    
    response = requests.delete(f'{url}{device_id}/', headers = http_headers, verify = False)

    if response.ok:
        print('device deleted successfully')


if __name__ == '__main__':
    main()
     

