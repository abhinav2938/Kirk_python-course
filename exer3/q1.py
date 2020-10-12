import re
from pprint import pprint

arp_details = '''
Protocol  Address      Age  Hardware        Type  Interface
Internet  10.220.88.1   67  0062.ec29.70fe  ARPA  Gi0/0/0
Internet  10.220.88.20  29  c89c.1dea.0eb6  ARPA  Gi0/0/0
Internet  10.220.88.22   -  a093.5141.b780  ARPA  Gi0/0/0
Internet  10.220.88.37 104  0001.00ff.0001  ARPA  Gi0/0/0
Internet  10.220.88.38 161  0002.00ff.0001  ARPA  Gi0/0/0
'''

arp_details = arp_details.strip()
arp_details = arp_details.splitlines()
arp_updated = []

for arp_entry in arp_details:
    if re.search(r'^Protocol.* Interface', arp_entry):
        #go back to the beginning of the loop 
        continue
    #assign junk values to placeholder and keep the useful values 
    _,ip_addr,_,mac_addr,_,interface = arp_entry.split()
    arp_dict = {'mac_addr': mac_addr, 'ip_addr': ip_addr,'interface':interface}
    arp_updated.append(arp_dict)

pprint(arp_updated)    
