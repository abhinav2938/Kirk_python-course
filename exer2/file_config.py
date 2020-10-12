from netmiko import ConnectHandler
from getpass import getpass
#from pprint import pprint

#password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()

password = getpass()
host = ['nxos1.lasthop.io', 'nxos2.lasthop.io']
for nxos in host:

    device = {
    'host': nxos,
    'username' : 'pyclass',
    'password' : password,
    'device_type' : 'cisco_ios',
   # 'fast_cli' : True
    }           
    ssh_connect = ConnectHandler(**device)
    print(ssh_connect.find_prompt())

    send_command = ssh_connect.send_config_from_file('vlan_file.txt')
    print('#'*100)
    print('sending config to device: {}'.format(nxos))
    print(send_command)
   # print('#'*100)
    ssh_connect.save_config()
    ssh_connect.disconnect()
