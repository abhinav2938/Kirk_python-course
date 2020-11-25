from my_devices import device_list
from my_functions import ssh_command
from datetime import datetime
import threading

if __name__ == '__main__':
    start_time = datetime.now()

    for a_device in device_list:
        my_thread =  threading.Thread(target = ssh_command, args = (a_device,))
        my_thread.start()
    
    main_thread = threading.currentThread()
    
    for some_thread in threading.enumerate():
        if some_thread != main_thread:
            print(some_thread)
            some_thread.join()

    end_time = datetime.now()
    print(end_time - start_time)
