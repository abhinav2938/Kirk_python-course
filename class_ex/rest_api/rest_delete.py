import requests
import json
import os
from pprint import pprint

from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category= InsecureRequestWarning)


if __name__ == '__main__':

    #token = '63aa375e2590159ca3171c5269931043b85d33cf'
    token = os.environ['NETBOX_TOKEN']
    url = 'http://netbox.lasthop.io/api/dcim/platforms/4/'
    #url = 'https://api.github.com/'
    http_headers = {'Content-type': 'application/json; version=2.4;'}
    if token:
        http_headers['authorization'] = 'Token {}'.format(token)

    response = requests.delete(url, headers = http_headers, verify = False)
    
    if response.ok:
        print('Device deleted successfully')
    
