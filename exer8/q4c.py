from jnpr.junos import Device
from getpass import getpass
from q2_jnpr_devices import srx2
from q2b import gather_routes
from jnpr.junos.op.routes import RouteTable
from pprint import pprint
from jnpr.junos.utils.config import Config


my_device = Device(**srx2)
my_device.open()
my_device.timeout = 60

gather_routes()

cfg = Config(my_device)
cfg.load(path= 'q4_config.conf', format = 'text', merge =True)
print(cfg.diff())
#cfg.commit()
#q4d
#cleanup the useless route
cfg.load('delete routing-options static route 203.0.113.5/32', format = 'set',merge= True)
cfg.load('delete routing-options static route 203.0.113.200/32', format = 'set',merge= True)
cfg.commit()

gather_routes()


