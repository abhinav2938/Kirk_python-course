from napalm import get_network_driver
from getpass import getpass
from pprint import pprint

device = dict(
    hostname= 'cisco3.lasthop.io',
    username = 'pyclass',
    password = getpass(),
    device_type = 'ios',
    )

device_type = device.pop('device_type')
driver = get_network_driver(device_type)
dev = driver(**device)

print()
print('\n\n>>>Test device open.')
dev.open()

print('\n some facts.')
pprint(dev.get_facts())

