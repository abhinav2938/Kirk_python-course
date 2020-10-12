from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from getpass import getpass

a_device = Device(host='srx2.lasthop.io', user= 'pyclass', password= getpass())
a_device.open()
a_device.timeout = 60


cfg = Config(a_device)
#print(cfg)
#print(type(cfg))

#to lock changes to config, so no one else can make any changes
cfg.lock()
#To unlock just use unlock

cfg.load(path = 'test_config.conf', format= 'text', merge= True)
print(cfg.diff())


#to rollback the change
#cfg.rollback(0)

#to commit, from candidate to running config
#cfg.commit(comment = 'making hostname change using pyez')


