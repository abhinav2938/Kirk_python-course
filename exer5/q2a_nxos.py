from jinja2 import StrictUndefined, FileSystemLoader
from jinja2.environment import Environment

env = Environment(undefined = StrictUndefined)
env.loader = FileSystemLoader('.')

nxos1 = {
    'intf_id' : 'Ethernet1/1',
    'ip_add' : '10.1.100.1',
    'subnet_mask' : 24,
}

nxos2 = {
    'intf_id' : 'Ethernet1/1',
    'ip_add' : '10.1.100.2',
    'subnet_mask' : 24
}

template_file = 'q2_temp.j2'
for device in (nxos1,nxos2):
    temp1 = env.get_template(template_file)
    out = temp1.render(**device)
    print(out)

