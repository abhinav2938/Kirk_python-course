import time
from concurrent.futures import ThreadPoolExecutor, wait
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
    
    #wait until all pending threads are done, its similar to join
    wait(future_list)

    #creating a loop to fetch the values from the future_list
    for future in future_list:
        print('Result: '+ future.result())

    end_time = datetime.now()
    print('\nTime taken:' + str(end_time - start_time))

