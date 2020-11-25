from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
from my_devices import device_list
from my_functions import ssh_command2

if __name__ == '__main__':
    start_time = datetime.now()
    max_threads = 4
   
    pool = ThreadPoolExecutor(max_threads)
    
    future_list = []
    for a_device in device_list:
        future = pool.submit(ssh_command2, a_device)
        future_list.append(future)

    #print the result as the thread is being processed
    for device in as_completed(future_list):
        print('Results:\n' + device.result())
        #print the time taken for each threads
        end_time = datetime.now()
        print('Time taken: \n' + str(end_time - start_time))
