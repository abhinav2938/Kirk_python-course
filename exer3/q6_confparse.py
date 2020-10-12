from netmiko import ConnectHandler
from ciscoconfparse import CiscoConfParse
from pprint import pprint
import re

cisco4_device = {
    'host': 'cisco4.lasthop.io',
    'username': 'pyclass',
    'password': '88newclass',
    'device_type': 'cisco_ios'
    }

ssh_connect = ConnectHandler(**cisco4_device)
send_command = ssh_connect.send_command('sh run')
with open('config_file.txt', 'w') as f:
    f.write(send_command) 

f = open('config_file.txt','r')
cisco_conf = CiscoConfParse(f)
#print('cisco_conf {}'.format(cisco_conf))
interfaces = cisco_conf.find_objects_w_child(parentspec= r'^interface', childspec=r'^\s+ip address')
#print('interfaces {}'.format(interfaces))
for intf in interfaces:
    print('Interface Line: {}'.format(intf.text))
    #new way to do it
    ip_addr = intf.re_search_children(r'^\s+ip address')[0].text
  
    # ip_addr = intf.re_search_children(r'^\s+ip address')
    #for i in ip_addr:
    print('ip addr: {}'.format(ip_addr))


