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
    #print(value)
    for key,addresses in value.items():
       # print('key:{}'.format(key))
       # print('value {}'.format(addresses))
        if re.search(r'^ipv4', key):
            for address,prefixes in addresses.items():
                #print('address: {}'.format(address))    
                #print('prefix: {}'.format(prefixes))
                #ipv4_list.append(address)
                for prefix,length in prefixes.items():
                 #   print('prefix_length: {}'.format(length))
                    ipv4_list.append('{}/{}'.format(address,length))
        elif re.search(r'^ipv6', key):
            for address,prefixes in addresses.items():
               # print('address: {}'.format(address))    
                #ipv6_list.append(address)
                for prefix,length in prefixes.items():
                  #  print('prefix_length: {}'.format(length))
                    ipv6_list.append('{}/{}'.format(address,length))
         #   addresses.append(ipv6_list)

pprint(ipv4_list)
pprint(ipv6_list)
