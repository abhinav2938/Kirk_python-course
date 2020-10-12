from jnpr.junos import Device
from getpass import getpass
from pprint import pprint
from lxml import etree
from q2_jnpr_devices import srx2

my_device = Device(**srx2)
my_device.open()
my_device.timeout = 60

#show version | display xml rpc (use this command on juniper)
#get-software-information

xml_out = my_device.rpc.get_software_information()
#print using etree as we did for xml, can also use decode instead of unicode
pprint(etree.tostring(xml_out,encoding = 'unicode'))


