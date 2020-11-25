# no need of using thread here

from netmiko import ConnectHandler
from datetime import datetime
#import threading
from my_devices import device_list

def show_ver(a_device):
    print('#'*80)
    print()
    ssh_conn = ConnectHandler(**a_device)
    output = ssh_conn.send_command_expect('show version')
    ssh_conn.disconnect()
    print('#'*80)
    print(output)
    print()

def main():
    start_time = datetime.now()
    
    #loop through each device and print the show_ver command
    for a_device in device_list:
       output = show_ver(a_device)

        # my_thread = threading.Thread(target = show_ver, args = (a_device,))
       # my_thread.start()
#
#        main_thread = threading.currentThread()
#    
#    for some_thread in threading.enumerate():
#        if some_thread != main_thread:
#            print(some_thread)
#            some_thread.join()
#
    end_time = datetime.now()
    print("Time taken: \n" +str(end_time - start_time))

if __name__ == '__main__':
    main() 
