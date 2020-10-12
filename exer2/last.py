from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint
import os
import time

password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()
device = {
    'host': 'cisco4.lasthop.io',
    'username' : 'pyclass',
    'password' : password,
    'device_type' : 'cisco_ios',
    'secret':password,
    'session_log': 'my_output.txt'
    }

ssh_connect = ConnectHandler(**device)
print(ssh_connect.find_prompt())

ssh_connect.config_mode()
print(ssh_connect.find_prompt())

ssh_connect.exit_config_mode()
print(ssh_connect.find_prompt())

ssh_connect.write_channel('disable\n')
time.sleep(2)
print(ssh_connect.read_channel())

ssh_connect.enable()
print(ssh_connect.find_prompt())


ssh_connect.disconnect()

