from jinja2 import StrictUndefined, FileSystemLoader
from jinja2.environment import Environment
from my_devices import nxos1,nxos2

env = Environment(undefined = StrictUndefined)
env.loader = FileSystemLoader('.')
print(f'nxos1{nxos1}')
nxos1 = {
    'intf_id' : 'Ethernet1/1',
    'ip_add' : '10.1.100.1',
    'subnet_mask' : 24,
    'local_as' : 22,
    'peer_ip' : '10.1.100.2',
}

nxos2 = {
    'intf_id' : 'Ethernet1/1',
    'ip_add' : '10.1.100.2',
    'subnet_mask' : 24,
    'local_as' : 22,
    'peer_ip' :  '10.1.100.1',
}

template_file = 'q2b.j2'
for device in (nxos1,nxos2):
    temp1 = env.get_template(template_file)
    out = temp1.render(**device)
    print(out)

