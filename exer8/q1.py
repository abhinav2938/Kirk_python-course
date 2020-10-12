from jnpr.junos import Device
from getpass import getpass
from pprint import pprint

device = Device(host = 'srx2.lasthop.io', user= 'pyclass', password= getpass())
device.open()
pprint(device.facts)
print()
print('device hostname facts')
pprint(device.facts['hostname'])
