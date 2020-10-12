from jnpr.junos import Device
from jnpr.junos.op.arp import ArpTable
from getpass import getpass
from pprint import pprint

a_device = Device(host = 'srx2.lasthop.io', user= 'pyclass', password = getpass())
a_device.open()

ports = ArpTable(a_device)
ports.get()

#pprint(ports)
pprint(ports.keys())
#pprint(ports.values())
