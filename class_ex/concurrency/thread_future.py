import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from netmiko import ConnectHandler
from my_devices import device_list

def ssh_conn(a_device):
    net_connect = ConnectHandler(**a_device)
    return net_connect.find_prompt()

def main():
    start_time = datetime.now()
    max_threads = 4

    pool = ThreadPoolExecutor(max_threads)
    future = pool.submit(ssh_conn, device_list[0])
    
    print(future.done())
    time.sleep(4)
    print(future.done())

    #waits until future is complete
    print('Results: '+ future.result())

    end_time = datetime.now()
    print('\nTime taken:' + str(end_time - start_time))

if __name__ == '__main__':
    main()
