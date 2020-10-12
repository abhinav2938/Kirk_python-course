from jnpr.junos import Device
from getpass import getpass
from lxml import etree
from pprint import pprint

junpr = {'host': 'srx2.lasthop.io', 'user': 'pyclass', 'password': getpass()}
a_device = Device(**junpr)
a_device.open()

#show version | display xml rpc (use this command on juniper)
#get-software-information

xml_out = a_device.rpc.get_software_information()
#print using etree as we did for xml, can also use decode instead of unicode
pprint(etree.tostring(xml_out, encoding = 'unicode'))
