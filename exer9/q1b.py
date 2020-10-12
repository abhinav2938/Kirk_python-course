from napalm import get_network_driver
from pprint import pprint
from my_devices import cisco3,arista1

def conn(my_dev):
    device = my_dev.pop('device_type')
    driver = get_network_driver(device)
    dev = driver(**my_dev)
    dev.open()
    return (dev)

list1 = [cisco3,arista1]

if __name__ == '__main__':
    for device in list1:
        conn_obj = conn(device)
        print('\n>>> Test device open')
        conn_obj.open()
        print(conn_obj)
        print('platform:')
        print(conn_obj.platform)
        print('\n>>> getting facts')
        out = conn_obj.get_facts()
        pprint(out)
