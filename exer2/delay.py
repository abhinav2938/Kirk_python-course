from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

device = {
    'host': 'nxos2.lasthop.io',
    'username' : 'pyclass',
    'password' : getpass(),
    'device_type' : 'cisco_ios',
    'global_delay_factor' : 2

    }

ssh_connect = ConnectHandler(**device)
print(ssh_connect.find_prompt())

start_time = datetime.now()
send_command = ssh_connect.send_command('show lldp neighbors detail')
end_time = datetime.now()
print('#'*30)
print(send_command)
print('#'*30)
exec_time = end_time - start_time

print('the execution time is: {}'.format(exec_time))

start_time = datetime.now()
send_command = ssh_connect.send_command('show lldp neighbors detail', delay_factor = 8)
end_time = datetime.now()
exec_time = end_time - start_time

print('*'*30)
print(send_command)
print('*'*50)
print('The execution time is:{} '.format(exec_time))

ssh_connect.disconnect()
