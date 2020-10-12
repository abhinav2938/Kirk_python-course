from pprint import pprint
from nxapi_plumbing import Device
from getpass import getpass
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

device = Device(
    api_format = 'jsonrpc',
    host = 'nxos1.lasthop.io',
    username = 'pyclass',
    password = getpass(),
    transport = 'https',
    port = '8443',
    verify = False
)

cmd = 'show interface Ethernet1/1'
output = device.show(cmd)
a = output['TABLE_interface']['ROW_interface']
for k,v in a.items():
    req = ['interface','state','eth_mtu']
    if k in req:
        print(k, v)


