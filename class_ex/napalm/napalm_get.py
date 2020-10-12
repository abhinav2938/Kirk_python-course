from napalm import get_network_driver
from getpass import getpass
from pprint import pprint

#supress  ssl warnings
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

password = getpass()
cisco3 = dict(
    hostname= 'cisco3.lasthop.io',
    username = 'pyclass',
    password = password,
    device_type = 'ios',
    )
#nneed to specify port for nexus devices
nxos1 = dict(
    hostname= 'nxos1.lasthop.io',
    username = 'pyclass',
    password = password,
    device_type = 'nxos',
    optional_args= {'port':8443}
    )

arista = dict(
    hostname= 'arista1.lasthop.io',
    username = 'pyclass',
    password = password,
    device_type = 'eos',
    )

my_device = arista
device = my_device.pop('device_type')
driver = get_network_driver(device)
dev = driver(**my_device)

print()
print('\n\n>>>Test device open.')
dev.open()

print('\n getter operations\n')
#output = dev.get_arp_table()
#output = dev.get_lldp_neighbors()
output = dev.get_facts()

pprint(output)

