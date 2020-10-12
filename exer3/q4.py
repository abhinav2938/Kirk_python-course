import re
import json
from pprint import pprint

filename = 'arista.json'
with open(filename, 'r') as f:
    arista = json.load(f)
new_dict = {}
#pprint(arista)
for key,value in arista.items():
    if key == 'ipV4Neighbors':
        for i in value:
        #better way of doing no need of extra loop
            mac_addr = i['hwAddress']
            ip_addr = i['address']      

        #another way of doing, first attempt   
            #for key,value in i.items():
               # print('key  {} '.format(key))
               # print('value  {} '.format(value))
             #   if key == 'hwAddress':
              #      mac_addr = value
               # if key == 'address':
                #    ip_addr = value

            new_dict[ip_addr] = mac_addr

pprint(new_dict)
