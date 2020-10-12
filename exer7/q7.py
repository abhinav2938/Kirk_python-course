from getpass import getpass
from pprint import pprint
from lxml import etree
from nxapi_plumbing import Device
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

device = Device(
    host = 'nxos1.lasthop.io',
    username = 'pyclass',
    password = getpass(),
    api_format = 'xml',
    transport = 'https',
    port = '8443',
    verify = False
)

cmd = 'show interface Ethernet1/1'
out = device.show(cmd)
#output = etree.tostring(out).decode()
print('Interface: {}; State: {}; MTU: {}'.format
            (out.find('.//interface').text,out.find('.//state').text,out.find('.//eth_mtu').text))

#q7b
def mul_cmd():
    cmd_list = ['show system uptime', 'show system resources']
    out = device.show_list(cmd_list)
    for entry in out:
        print(etree.fromstring(entry).decode())
        input('Hit enter: ')
#mul_cmd()

#q7c

cfg_commands = [
    'int lo101',
    'description math',
    'int lo102',
    'description science',        
    ]

#out = device.config_list(cfg_commands)
#for cmd in out:  
 #   print(etree.tostring(cmd).decode())   
