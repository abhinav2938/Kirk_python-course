import yaml
import re
from pprint import pprint

arp_data = '''
Protocol  Address      Age  Hardware        Type  Interface
Internet  10.220.88.1   67  0062.ec29.70fe  ARPA  Gi0/0/0
Internet  10.220.88.20  29  c89c.1dea.0eb6  ARPA  Gi0/0/0
Internet  10.220.88.22   -  a093.5141.b780  ARPA  Gi0/0/0
Internet  10.220.88.37 104  0001.00ff.0001  ARPA  Gi0/0/0
Internet  10.220.88.38 161  0002.00ff.0001  ARPA  Gi0/0/0
'''

arp = arp_data.strip().splitlines()
#arp = arp.splitlines()
pprint(f'arp: {arp}')
my_list = []
for line in arp:
    my_dict = {}
    pprint(f'the first line is: {line}')
    if re.search(r'^Protocol.* Interface',line):
        continue
    pprint(f'the line is : {line}')
    _,ip_addr,_,mac_addr,_,intf = line.split()
    my_dict['ip'] = ip_addr
    my_dict['mac_addr'] = mac_addr
    my_dict['intf'] = intf
    my_list.append(my_dict)

print(f'my_list:{my_list}')

