from jnpr.junos import Device
from getpass import getpass
from q2_jnpr_devices import srx2
from jnpr.junos.op.routes import RouteTable
from pprint import pprint
from jnpr.junos.utils.config import Config


my_device = Device(**srx2)
my_device.open()
my_device.timeout = 60

ports = RouteTable(my_device)
ports.get()
#pprint(ports.items())

cfg = Config(my_device)
cfg.load(path= 'q4_config.conf', format = 'text', merge =True)
print(cfg.diff())




