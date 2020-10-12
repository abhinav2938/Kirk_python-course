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
#print(cisco_obj)
list1 = []

remote_ip = cisco_obj.find_objects_w_child(parentspec= r'^\s+neighbor ', childspec = r'^\s+remote-as ')
#print('remote_ip {}'.format(remote_ip)) 
for ip in remote_ip:
    ip_neig = '{}'.format(ip.text)
   #print('ip_neig: {}'.format(ip_neig))
    ip_add = ip_neig.split(' ')[2]
    remote_as = ip.re_search_children(r'\s+remote-as ')
    re_as = '{}'.format(remote_as[0].text)
    as_number = re_as.split(' ')[3]
    tup1 = (ip_add, as_number)
    list1.append(tup1)

print('BGP Peers: \n{}'.format(list1))   
