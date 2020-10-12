import pyeapi
from getpass import getpass
import yaml

def load_yaml():
    with open('q2.yml') as f:
        device = f.read()
        return(yaml.load(device))
    raise ValueError("Reading YAML file failed")

def main():
    
    device = load_yaml()
    print('device from yaml {}'.format(device))

    for name,device_dict in device.items():
        device_dict['password'] = getpass()
        connection = pyeapi.client.connect(**device_dict)
        device = pyeapi.client.Node(connection)
        output = device.enable(['show ip arp'])
       # print(output)
        #printing the arp ip_Add vs mac_addr

        list1 = output[0]['result']['ipV4Neighbors']
        for arp in list1:
            ip_add = arp['address']
            mac_add = arp['hwAddress']
            print('{:^15} ---> {:^15}'.format(ip_add,mac_add))

if __name__ == '__main__':
    main()

