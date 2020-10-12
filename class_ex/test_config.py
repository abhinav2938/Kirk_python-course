from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

device = {
        'host': 'cisco3.lasthop.io',
        'username' : 'pyclass',
        #'username': 'testuser',
        #'use_keys': True,
        #'key_file': '/home/kbyers/.ssh/test_rsa',
        'password' : getpass(),
        'device_type' : 'cisco_ios_telnet',
        #'fast_cli' : True
        }

ssh_connect = ConnectHandler(**device)
print(ssh_connect.find_prompt())

config_com = [
        'logging buffered 30000',
        'clock timezone EST -5 0'
]

#output = ssh_connect.send_config_set(config_com)
#pprint(output)

#save_out = ssh_connect.save_config()
#print(save_out)

#ssh_connect.disconnect()
