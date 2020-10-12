from getpass import getpass
from q2_jnpr_devices import srx2
from jnpr.junos import Device
from pprint import pprint
from jnpr.junos.op.routes import RouteTable
from jnpr.junos.op.arp import ArpTable

def check_connected():
    pprint(my_device.connected)
   # pprint(my_device.facts)

def gather_routes():
    ports = RouteTable(my_device)
    ports.get()
    pprint(ports.items())
    return ports

def gather_arp_table():
    ports = ArpTable(my_device)
    ports.get()
    #print('ARP table entry')
    #pprint(ports)
    #pprint(ports.items())
    return ports

def print_output(dev,route,arp):
    my_device = {}
    my_device['hostname'] = dev.hostname
    my_device['connected_port'] = dev.port
    my_device['connected_user'] = dev.user
    my_device['route-table'] = route.items()
    my_device['arp-table'] = arp.items()
    pprint(my_device)
    

my_device = Device(**srx2)
my_device.open()
if __name__ == '__main__':
    route = gather_routes()
    arp = gather_arp_table()
    print_output(my_device,route, arp)

    
