from q1b import conn
from pprint import pprint
from getpass import getpass
from my_devices import devices


def my_functions():
    for device in devices:
        conn_obj = conn(device)
        print('\n>>> Test device open')
        conn_obj.open()
        #print('\n>>> getting facts')
        #out = conn_obj.get_facts()
        hostname = device['hostname']
        #print(f'\n>> getting ARP table for {hostname}')
        #out = conn_obj.get_arp_table()
        #q2c
        print(f'\n>> getting ntp_peers for {hostname}')
        try:
            out = conn_obj.get_ntp_peers()
            pprint(out)   
        except :
            print('wrong command')


def create_backup(conn):
    print('\n>>> get the current config')
    backup = conn.get_config()
    filename = f'run_config_{conn.hostname}.txt'
    with open(filename, 'w') as f:
        out= connect_obj.get_config()
        #pprint(out)
        f.write(out['running'])

def create_checkpoint(conn):
    print('\n>> get the checkpoint ')
    chk = conn._get_checkpoint_file()
    filename = 'checkpnt_nx.txt'
    with open(filename, 'w') as f:
        f.write(chk)

    
if __name__ == '__main__':    
    for device in devices:
        connect_obj = conn(device)
        create_backup(connect_obj)    


    #my_functions()
 
