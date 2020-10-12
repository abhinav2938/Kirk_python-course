from pprint import pprint
from jinja2 import StrictUndefined, FileSystemLoader
from jinja2.environment import Environment
import time
import re

from my_devices import nxos1, nxos2
from netmiko import ConnectHandler

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader('.')

j2_nxos1 = {
        'intf_id': 'Ethernet1/1',
        'ip_add': '10.1.100.1',
        'subnet_mask': 24,
        'local_as': 22,
        'peer_ip': '10.1.100.2',
    }
j2_nxos2 = {
        'intf_id': 'Ethernet1/1',
        'ip_add': '10.1.100.2',
        'subnet_mask': 24,
        'local_as': 22,
        'peer_ip': '10.1.100.1'
    }

template_file = 'q2b.j2'
    # adding jinja2 variables in the Nx-os dictionary
nxos1['j2_vars'] = j2_nxos1
nxos2['j2_vars'] = j2_nxos2

print(f'nxos1: {nxos1}')
for device in (nxos1, nxos2):
    temp_device = device.copy()
    bgp_var = temp_device.pop('j2_vars')
    #print(bgp_var)
    template = env.get_template(template_file)
    out = template.render(**bgp_var)
    print(out)

        # set up the ssh connection to the device
    cfg_new = [out.strip() for out in out.splitlines()]
   #pprint(f'cfg_new: {cfg_new}')
    print(f'temp_device: {temp_device}')
    ssh_conn = ConnectHandler(**temp_device)
    send_config = ssh_conn.send_config_set(cfg_new)
    print(send_config)

#test the configuration and ping
# give time for BGP config
sleep_time = 1
print(f'sleeping for {sleep_time} seconds')
time.sleep(sleep_time)

temp_device = nxos1.copy()
temp_device.pop('j2_vars')

#ping the neighbor
for device in (nxos1,):
    ssh_conn = ConnectHandler(**temp_device)
    #print(f'device :{device}')
    peer_add = device['j2_vars']['peer_ip']
    out = ssh_conn.send_command(f'ping {peer_add}')
    print (out)
    if ('64 bytes from ' not in out):
        print('ping failed')
    else:
        print('ping successful')

    #test bgp
    bgp_verify_comm = f'sh ip bgp summary | i {peer_add}'
    ssh_conn = ConnectHandler(**temp_device)
    out = ssh_conn.send_command(bgp_verify_comm)
    print(out)
    # use re to check the last digit in output is integer
    match = re.search(r'\s+(\S+)\s*$', out)
    pfx_rcvd= match.group(1)
    print(f'match: {pfx_rcvd}')
    try:
        int(pfx_rcvd)
        print(f'BGP peer successfully done and prefix received {pfx_rcvd}')
    except ValueError:
        print('BGP failed to reach established state')


#disconnect devices
for devices in (nxos1,nxos2):
    ssh_conn = ConnectHandler(**temp_device)
    ssh_conn.disconnect()

print('\n\n')

    




