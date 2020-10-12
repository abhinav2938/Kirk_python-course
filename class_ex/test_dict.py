from netmiko import ConnectHandler
from getpass import getpass

device = {
        'host': 'cisco3.lasthop.io',
        'username': 'pyclass',
        'password': getpass(),
        'device_type' : 'cisco_ios'
        }

ssh_connect = ConnectHandler(**device)
print(ssh_connect.find_prompt())

output = ssh_connect.send_command('sh ip arp', use_textfsm = True)
print(output)
