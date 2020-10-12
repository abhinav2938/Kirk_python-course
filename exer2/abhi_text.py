from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint
import os

#password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()
device = {
    'host': 'cisco4.lasthop.io',
    'username' : 'pyclass',
    'password' : getpass(),
    'device_type' : 'cisco_ios',
    #'global_delay_factor' : 2

    }

ssh_connect = ConnectHandler(**device)
print(ssh_connect.find_prompt())

send_command1 = ssh_connect.send_command('show lldp neighbors', use_textfsm = True)
print('#'*100)
pprint(send_command1)
print('#'*100)

send_command2 = ssh_connect.send_command('show version', use_textfsm = True)
print('*'*100)
pprint(send_command2)
print('*'*100)

print("The datastructure for 'sh lldp neigh' is {}".format(type(send_command1)))

print("The interface is {}".format(send_command1[0]['neighbor_interface']))
ssh_connect.disconnect()

