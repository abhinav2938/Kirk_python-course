from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

device = {
        'host': 'cisco4.lasthop.io',
        'username' : 'pyclass',
        #'username': 'testuser',
        #'use_keys': True,
        #'key_file': '/home/kbyers/.ssh/test_rsa',
        'password' : getpass(),
        'device_type' : 'cisco_ios',
        #'fast_cli' : True
        }

ssh_connect = ConnectHandler(**device)
print(ssh_connect.find_prompt())

send_command = ssh_connect.send_command('sh ip arp', use_textfsm = True)
for ip in send_command: 
        print(ip['address']) 
        print(ip['interface']) 
        print('#'*30) 
        print() 

ssh_connect.disconnect()
