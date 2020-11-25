import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from netmiko import ConnectHandler
from my_devices import device_list

def ssh_conn(a_device):
    net_connect = ConnectHandler(**a_device)
    return net_connect.find_prompt()

if __name__ == '__main__':
    start_time = datetime.now()
    max_threads = 4

    pool = ThreadPoolExecutor(max_threads)

    future_list = []
    for a_device in device_list:        
        future = pool.submit(ssh_conn, a_device)
        future_list.append(future)

    #print the result as completed
    for future in as_completed(future_list):
        print('Result: '+ future.result())
        end_time = datetime.now()
        print('\nTime taken:' + str(end_time - start_time))

