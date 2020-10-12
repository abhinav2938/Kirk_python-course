from netmiko import ConnectHandler
from getpass import getpass

password = getpass()
device1 = {
    'host': 'cisco3.lasthop.io',
    'username': 'pyclass',
    'password': password,
    'device_type':'cisco_ios'
    }

device2 = {
        'host': 'cisco4.lasthop.io',
        'username': 'pyclass',
        'password': password,
        'device_type':'cisco_ios'
       }

device_list = [device1,device2]
for device in device_list:
    ssh_connect = ConnectHandler(**device)
    print(ssh_connect.find_prompt())
    if device == device2:
        output = ssh_connect.send_command('sh version')
        with open('show_ver.txt', 'w')as f:
            f.write(output)


