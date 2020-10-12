import json
import re
from pprint import pprint

with open('nxos.json', 'r') as f:
    var1 = json.load(f)

#pprint(var1)
ipv4_list = []
ipv6_list = []

for key,value in var1.items():
    for addr_type, value in value.items():
            if addr_type == 'ipv4':
                for addr, pfx_len in value.items():
                    pfx = pfx_len['prefix_length']
                    ipv4_list.append('{}/{}'.format(addr,pfx))

            if addr_type == 'ipv6':
                for addr, pfx_len in value.items():
                    pfx = pfx_len['prefix_length']
                    ipv6_list.append('{}/{}'.format(addr,pfx))

pprint(f'ipv4_list: {ipv4_list}')
print()
pprint(f'ipv6_list: {ipv6_list}')
