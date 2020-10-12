from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

#password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()
device = {
    'host': 'cisco3.lasthop.io',
    'username' : 'pyclass',
    'password' : getpass(),
    'device_type' : 'cisco_ios',
    'fast_cli' : True
    }

config_command = ['ip name-server 1.1.1.1', 'ip name-server 1.0.0.1', 'ip domain-lookup']
ssh_connect = ConnectHandler(**device)
print(ssh_connect.find_prompt())

send_command = ssh_connect.send_config_set(config_command)
print('#'*100)
pprint(send_command)
print('#'*100)


ssh_connect.disconnect()

