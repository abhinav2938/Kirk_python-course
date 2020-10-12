from netmiko import ConnectHandler,file_transfer
from getpass import getpass

device = {
        'host': 'nxos1.lasthop.io',
        'username': 'pyclass',
        'password': getpass(),
        'device_type' : 'cisco_nxos'
        }

source_file = 'testx.txt'
dest_file = 'test_abhi.txt'
direction = 'put'
file_system = 'bootflash:'

#create the netmiko ssh connection
ssh_connect = ConnectHandler(**device)
print(ssh_connect.find_prompt())
#create a dict for the transfer file
transfer_dict = file_transfer(
    ssh_connect,
    source_file = source_file,
    dest_file = dest_file,
    direction = direction,
    file_system = file_system,
    overwrite_file = True
)
    
print(transfer_dict)
