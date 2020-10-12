from pprint import pprint
from netmiko import ConnectHandler
import yaml

filename = 'devices.yml'
with open(filename, 'r') as f:
    devices = yaml.load(f)
#pprint('devices: {}'.format(devices))
#new_dict = {}

#for key,value in devices.items():
   # if key == 'cisco3':
      #  print('This is the one')
        #new_dict = value

#more better method
cisco3 = devices['cisco3']
#new_dict = cisco3

pprint(cisco3)

ssh_connect = ConnectHandler(**cisco3)
send_command = ssh_connect.find_prompt()
print(send_command)
        
