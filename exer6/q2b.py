import pyeapi
from getpass import getpass
import yaml
from my_func import read_yaml, output_print


def main():
    
    device = read_yaml()
    print('device from yaml {}'.format(device))

    for name,device_dict in device.items():
        device_dict['password'] = getpass()
        connection = pyeapi.client.connect(**device_dict)
        device = pyeapi.client.Node(connection)
        output = device.enable(['show ip arp'])
       # print(output)
        #printing the arp ip_Add vs mac_addr

        list1 = output[0]['result']['ipV4Neighbors']
        output_print(list1)

if __name__ == '__main__':
    main()
