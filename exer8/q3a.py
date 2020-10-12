from getpass import getpass
from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from pprint import pprint
from q2_jnpr_devices import srx2

my_device = Device(**srx2)
my_device.open()
my_device.timeout = 60

cfg = Config(my_device)
cfg.lock()

cfg.load('set system host-name test123', format='set', merge= True)
print('difference in config')
print(cfg.diff())
cfg.rollback(0)
print('config rolled back, diff now')
print(cfg.diff())

