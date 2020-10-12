#!/usr/bin/env python
from netmiko import ConnectHandler
from getpass import getpass
#from keyboard import press

device1 = {
    'host' : 'cisco3.lasthop.io',
    'username' : 'pyclass',
    'password' : getpass(),
    'device_type': 'cisco_ios',
    'global_delay_factor' : 4
    }

ssh_connect = ConnectHandler(**device1)
print(ssh_connect.find_prompt())

output = ssh_connect.send_command('sh ip int br')
print(output)
