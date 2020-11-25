import requests
from pprint import pprint

from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category = InsecureRequestWarning)

if __name__ == '__main__':
    url = 'https://netbox.lasthop.io/api/'
    http_headers = {}
    http_headers['accept'] = 'application/json; version = 2.4;'

    response = requests.get(url, headers = http_headers, verify = False)
    pprint(response.status_code)
    print()
    print('*'*80)
    pprint(response.text)
    print()
    print('#'*80)
    pprint(response.json())
    print()
    print('*'*80)
    pprint(dict(response.headers))
