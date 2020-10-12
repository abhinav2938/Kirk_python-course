import pyeapi
import ipdb
from getpass import getpass

ipdb.set_trace()
#creating the connection object
connection = pyeapi.client.connect(
    transport = 'https',
    host = 'arista8.lasthop.io',
    username = 'pyclass',
    password = getpass(),
    port = '443'
)

#creating a node object with the help of connection
device = pyeapi.client.Node(connection)

    

