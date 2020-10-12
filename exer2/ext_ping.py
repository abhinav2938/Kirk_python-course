from netmiko import ConnectHandler
from getpass import getpass

device = {
    'host': 'cisco4.lasthop.io',
    'username' : 'pyclass',
    'password' : getpass(),
    'device_type' : 'cisco_ios',
    'fast_cli' : True
    }

ssh_connect = ConnectHandler(**device)
print(ssh_connect.find_prompt())

send_command = ssh_connect.send_command_timing('ping',strip_prompt=False, strip_command=False)
send_command += ssh_connect.send_command_timing('\n',strip_prompt=False, strip_command=False)
send_command += ssh_connect.send_command_timing('8.8.8.8',strip_prompt=False, strip_command=False)
send_command += ssh_connect.send_command_timing('\n',strip_prompt=False, strip_command=False)
send_command += ssh_connect.send_command_timing('\n',strip_prompt=False, strip_command=False)
send_command += ssh_connect.send_command_timing('\n',strip_prompt=False, strip_command=False)
send_command += ssh_connect.send_command_timing('\n',strip_prompt=False, strip_command=False)
send_command += ssh_connect.send_command_timing('\n',strip_prompt=False, strip_command=False)


print(send_command)

ssh_connect.disconnect()

