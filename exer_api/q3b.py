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
    for i in result: 
        device = i['display_name'] 
        location = i['site']['name'] 
        vendor = i['device_type']['manufacturer']['name'] 
        status = i['status']['label'] 
        print('-'*80) 
        print(device) 
        print('-'*20) 
        print('Location: {}'.format(location)) 
        print('Vendor: {}'.format(vendor)) 
        #print('Status: {}'.format(status))
    #can also print like this 
        print(f'Status: {status}')
        print('-'*80)
        print() 
