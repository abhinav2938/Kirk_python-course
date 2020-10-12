from pprint import pprint
from getpass import getpass
from jnpr.junos import Device

srx2 = {
    'host': 'srx2.lasthop.io',
    'user': 'pyclass',
    'password': getpass(),
     }

if __name__ == '__main__':
    my_device = Device(**srx2)
    my_device.open()
    pprint(my_device.facts)
