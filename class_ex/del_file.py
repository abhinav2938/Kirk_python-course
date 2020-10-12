#!/usr/bin/env python
from netmiko import ConnectHandler
from getpass import getpass
from keyboard import press

device1 = {
    'host' : 'cisco3.lasthop.io',
    'username' : 'pyclass',
    'password' : getpass(),
    'device_type': 'cisco_ios'
    }

ssh_connect = ConnectHandler(**device1)
command = 'delete flash:/test9.txt'
output = ssh_connect.send_command(command, expect_string= r'[test9.txt]')
output += ssh_connect.send_command('y')
print (output)
