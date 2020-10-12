import requests
import json
from pprint import pprint
from getpass import getpass

from urllib3.exceptions import InsecureRequestWarning
import ipdb

#to disable the ssl warning
requests.packages.urllib3.disable_warnings(category = InsecureRequestWarning)

if __name__ == "__main__" :
    ipdb.set_trace()

    http_header = {'content_type': 'application/json/rpc'}
    host = 'arista8.lasthop.io'
    port = 443
    username = 'pyclass'
    password = getpass()

    url = "https://{}:{}/command-api".format(host,port)
    
    command = [
        'disable',
        {'cmd': 'enable', 'input': '' },
        'configure terminal',
        'vlan 100',
        'name grn'
    ]
           
    json_payload = {
        'jsonrpc' : '2.0',
        'method' : 'runCmds',
        'params' : {'version':1, 'cmds': command, 'format': 'json'},
        'id': '1'
        }
    
    json_data = json.dumps(json_payload)
    http_header['content_length'] = str(len(json_data))
 
    #create a http post using the request library
    response = requests.post(
        url,
        headers = http_header,
        auth = (username,password),
        data = json_data,
        verify = False
    )
    response = response.json()
     
    print()
    pprint(response)
    print()
