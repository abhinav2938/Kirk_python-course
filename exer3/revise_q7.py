from ciscoconfparse import CiscoConfParse
from pprint import pprint
import re

bgp = '''
router bgp 44
 bgp router-id 10.220.88.38
 address-family ipv4 unicast
 !
 neighbor 10.220.88.20
  remote-as 42
  description pynet-rtr1
  address-family ipv4 unicast
   route-policy ALLOW in
   route-policy ALLOW out
  !
 !
 neighbor 10.220.88.32
  remote-as 43
  address-family ipv4 unicast
   route-policy ALLOW in
   route-policy ALLOW out
'''
bgp = bgp.strip().splitlines()
bgp_conf = CiscoConfParse(bgp)
pprint (f'bgp_conf_parse: {bgp_conf}')

bgp_list = []
#for line in bgp_conf:
match = bgp_conf.find_objects_w_child(parentspec = r'^\s+neighbor.*', childspec = r'^\s+remote-as.*')
pprint('match: {}'.format(match))
for line in match:
    rem_as = line.re_search_children(r'^\s+remote-as')
    _,ip_add = line.text.split()
    _,re_as = rem_as[0].text.split()
    tup = (ip_add,re_as)
    print('tuple:{}'.format(tup))
    bgp_list.append(tup)

print(bgp_list)



