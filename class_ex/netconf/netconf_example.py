from ncclient import manager
from getpass import getpass
from pprint import pprint
import ipdb

conn = manager.connect(
    host = 'srx2.lasthop.io',
   #host = 'cisco3.lasthop.io',
#    device_params= {'name': 'junos'},
    timeout = 60,
    port = 830,
    username = 'pyclass',
    password = getpass(),
    hostkey_verify = False,
    allow_agent = False,
    look_for_keys= False,
)

#ipdb.set_trace()
config = conn.get_config(source = 'running')
config_xml = config.data_xml
print(config_xml) 

