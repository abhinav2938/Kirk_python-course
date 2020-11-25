from concurrent.futures import ProcessPoolExecutor
from datetime import datetime
from my_devices import device_list
from my_functions import ssh_command3

if __name__ == '__main__':
    start_time = datetime.now()
    max_process = 4

    with ProcessPoolExecutor(max_process) as pool:
        result_gen = pool.map(ssh_command3, device_list)
        
        #print the results
        for result in result_gen:
            print(result)
            end_time = datetime.now()
            print('Time taken: \n' + str(end_time - start_time))
