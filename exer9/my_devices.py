from getpass import getpass
#from napalm import get_network_driver
#from pprint import pprint

password = getpass()

cisco3 = dict(
    hostname =  'cisco3.lasthop.io',
    username = 'pyclass',
    password = password,
    device_type = 'ios'
    )

arista1 = dict(
    hostname = 'arista1.lasthop.io',
    username = 'pyclass',
    password = password,
    device_type = 'eos',
    )

nxos1 = dict(
    hostname = 'nxos1.lasthop.io',
    username = 'pyclass',
    password = password,
    device_type = 'nxos',
    optional_args = {'port': 8443}
    )

devices = [cisco3,arista1, nxos1]
