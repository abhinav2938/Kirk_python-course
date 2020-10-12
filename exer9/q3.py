from pprint import pprint
from getpass import getpass
from my_devices import devices
from q2 import my_functions
from q1b import conn

for device in devices:
    conn_obj = conn(device)
    print(f'\n>> connected to device: {conn_obj.hostname}')
    if conn_obj.hostname == 'cisco3.lasthop.io':
        print('\n>>> Adding loopbacks to Cisco3')
        output = conn_obj.load_merge_candidate(filename= 'cisco3.lasthop.io-loopbacks')
        pprint(conn_obj.compare_config())
        print('commiting the changes')
        conn_obj.commit_config()
        print('comparing the config after commit')
        pprint(f'config diff: {conn_obj.compare_config()}')

    else:
        print('adding loopbacks to arista1')
        output = conn_obj.load_merge_candidate(filename= 'arista1.lasthop.io-loopbacks')
        pprint(conn_obj.compare_config())
        print('commiting the changes')
        conn_obj.commit_config()
        print('comparing the config after commit')
        pprint(f'config diff: {conn_obj.compare_config()}')

