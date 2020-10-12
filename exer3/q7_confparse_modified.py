from pprint import pprint
from ciscoconfparse import CiscoConfParse
import re

bgp_nbr = '''
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
bgp_nbr = bgp_nbr.strip()
bgp_nbr = bgp_nbr.splitlines()
cisco_obj = CiscoConfParse(bgp_nbr)
list1 = []

remote_ip = cisco_obj.find_objects_w_child(parentspec= r'^\s+neighbor ', childspec = r'^\s+remote-as ')
for ip in remote_ip:
    
   #using placehlder to assign values to the required field
    _,ip_neig = ip.text.split()
    remote_as = ip.re_search_children(r'\s+remote-as ')
    _,re_as = remote_as[0].text.split()

    tup1 = (ip_neig, re_as)
    list1.append(tup1)

print('BGP Peers: \n{}'.format(list1))   
