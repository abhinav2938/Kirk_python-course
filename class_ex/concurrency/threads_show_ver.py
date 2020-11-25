'''
use threads and Netmiko to connect to each device and print the output 
of 'show version' on each device. Record the amount of time required to do it.
'''

from __future__ import print_function, unicode_literals
import threading
from datetime import datetime
from netmiko import ConnectHandler
from my_devices import device_list as devices

def show_version(a_device):
    '''execute show version command using Netmiko.'''
    print()
    print('#' * 80)
    remote_connect = ConnectHandler(**a_device)
    output = remote_connect.send_command_expect('show version')
    remote_connect.disconnect()
    print(output)
    print('#' * 80)
    print()
    
def main():
    start_time = datetime.now()
    
    #loop through each device and print show_ver
    for a_device in devices:
        my_thread = threading.Thread(target= show_version, args= (a_device,))
        my_thread.start()
    
    main_thread = threading.currentThread()
    for some_thread in threading.enumerate():
        if some_thread != main_thread:
            print(some_thread)
            some_thread.join()

    print('\n Elapsed time:' + str(datetime.now() - start_time))

if __name__ == '__main__':
    main()    
