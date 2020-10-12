import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lxml import etree
from pprint import pprint
from getpass import getpass
from nxapi_plumbing import Device

#to disable the ssl warning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

device = Device(
    api_format = 'xml',
    host = 'nxos1.lasthop.io',
    username = 'pyclass',
    password = getpass(),
    transport = 'https',
    port = '8443',
    #since self-signed certificate so verify is false
    verify = False
)

#output = device.show('show version')
#we use decode to convert byte to string
#print(etree.tostring(output).decode())

cmds = [
    'show version',
    'show hostname',
    'show lldp neighbors'
    ]

output = device.show_list(cmds)
for entry in output:
    print(etree.tostring(entry).decode())
    input('Hit enter to continue: ')

cmd = ['show version']
#raw_text returns in string format instead of a structured data

output = device.show_list(cmd, raw_text = True) 
print(etree.tostring(output[0]).decode())

output = device.save()
print(output)


cfg_cmds = [
    'interface vlan 2',
  #  'name new',
    ]
output = device.config_list(cfg_cmds)
print(etree.tostring(output[0]).decode())
