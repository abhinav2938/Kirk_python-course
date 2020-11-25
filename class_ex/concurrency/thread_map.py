#we can use either ThreadPoolExecutor or the ProceesPoolExecutor
from concurrent.futures import ProcessPoolExecutor
from datetime import datetime
from netmiko import ConnectHandler
from my_devices import device_list

def ssh_conn(a_device):
    device = {}
    connect = ConnectHandler(**a_device)
    key = connect.host
    value = connect.find_prompt()
    device[key] = value
    return device

if __name__ == '__main__':
    start_time = datetime.now()
    max_threads = 4

    with ProcessPoolExecutor(max_threads) as pool:
        pool_map = pool.map(ssh_conn, device_list)

        #print the result
        for result in pool_map:
            print(result)
            end_time = datetime.now()
            print('Time taken: \n' + str(end_time - start_time)) 
