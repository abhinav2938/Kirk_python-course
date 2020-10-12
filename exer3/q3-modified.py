import json
from pprint import pprint
import re

filename = 'nxos.json'
with open(filename, 'r') as f:
    nxos = json.load(f)
#pprint(nxos)

ipv4_list = []
ipv6_list = []
for interface,value in nxos.items():
    for key,addresses in value.items():
        if key == 'ipv4':
            for address,prefixes in addresses.items():
                #extracting the prefix_length from the dict and using it
                pfx_ln = prefixes['prefix_length']
                ipv4_list.append('{}/{}'.format(address,pfx_ln))
        elif key == 'ipv6':
            for address,prefixes in addresses.items():
                pfx_ln = prefixes['prefix_length']
                ipv6_list.append('{}/{}'.format(address,pfx_ln))

pprint(ipv4_list)
pprint(ipv6_list)
