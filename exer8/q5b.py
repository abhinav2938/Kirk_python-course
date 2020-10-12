from jnpr.junos import Device
from getpass import getpass
from pprint import pprint
from lxml import etree
from q2_jnpr_devices import srx2

my_device = Device(**srx2)
my_device.open()
my_device.timeout = 60

#show interfaces terse | display xml rpc (use this command on juniper)
#get-interface-information

xml_out = my_device.rpc.get_interface_information(terse= True)
#print using etree as we did for xml, can also use decode instead of unicode
print(etree.tostring(xml_out, encoding = 'unicode'))

#q5c

#xml_out = my_device.rpc.get_interface_information(interface_name="fe-0/0/7", terse= True, normalize = True)
#print using etree as we did for xml, can also use decode instead of unicode
#print(etree.tostring(xml_out,pretty_print = True, encoding = 'unicode'))


