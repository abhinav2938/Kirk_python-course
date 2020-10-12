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

send_command = ssh_connect.send_command('ping',expect_string=r'Protocol',strip_prompt=False, strip_command=False)
send_command += ssh_connect.send_command('\n', expect_string = r'Target',strip_prompt=False, strip_command=False)
send_command += ssh_connect.send_command('8.8.8.8', expect_string = r'Repeat',strip_prompt=False, strip_command=False)
send_command += ssh_connect.send_command('\n', expect_string = r'Datagram',strip_prompt=False, strip_command=False)
send_command += ssh_connect.send_command('\n', expect_string = r'Timeout',strip_prompt=False, strip_command=False)
send_command += ssh_connect.send_command('\n', expect_string = r'Extended',strip_prompt=False, strip_command=False)
send_command += ssh_connect.send_command('\n', expect_string = r'Sweep',strip_prompt=False, strip_command=False)
send_command += ssh_connect.send_command('\n', expect_string = r'#',strip_prompt=False, strip_command=False)
print(send_command)

ssh_connect.disconnect()

