import pyeapi
from getpass import getpass
from pprint import pprint

connection = pyeapi.client.connect(
    transport = 'https',
    host = 'arista3.lasthop.io',
    username = 'pyclass',
    password = getpass(),
    port = 443,
)

#create a node object with the help of connection
device = pyeapi.client.Node(connection)
#you can send command in list if more than one
output = device.enable('show ip arp')
#pprint(output)

list1 = output[0]['result']['ipV4Neighbors']
for arp in list1:
    ip_add = arp['address']
    mac_add = arp['hwAddress']

    print('{:^15} ---> {:^15}'.format(ip_add,mac_add))
