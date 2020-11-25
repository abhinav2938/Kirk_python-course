import requests
import os
from pprint import pprint

from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category= InsecureRequestWarning)


if __name__ == '__main__':

    #token = '63aa375e2590159ca3171c5269931043b85d33cf'
    token = os.environ['NETBOX_TOKEN']
    url = 'https://netbox.lasthop.io/api/dcim/devices/'
    #url = 'https://api.github.com/'
    http_headers = {'accept': 'application/json; version=2.4;'}
    if token:
        http_headers['authorization'] = 'Token {}'.format(token)

    response = requests.get(url, headers = http_headers, verify = False)
    response = response.json()
    
    print()
    pprint(response)
    print()
