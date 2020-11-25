
from multiprocessing import Process

from datetime import datetime
from netmiko import ConnectHandler
from my_devices import device_list as devices

def show_ver(a_device):
    remote_conn = ConnectHandler(**a_device)
    output = remote_conn.send_command_expect('show version')
    remote_conn.disconnect()
    print()
    print('#'*80)
    print(output)
    print('#'*80)

def main():
    start_time = datetime.now()

    procs = []
    #loop through device and print show_version
    for a_device in devices:
        my_proc = Process(target = show_ver, args = (a_device,))
        my_proc.start()
        procs.append(my_proc)

    for a_proc in procs:
        a_proc.join()

    print('\n Elapsed time: ' + str(datetime.now() - start_time))

if __name__ == '__main__':
    main()
