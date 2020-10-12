import pyeapi
from getpass import getpass
import yaml
from pprint import pprint
from my_func import read_yaml, output_print

def main():
    device = read_yaml()

    for name, device_dict in device.items():
        device_dict['password'] = getpass()
        connection = pyeapi.client.connect(**device_dict)
        device =  pyeapi.client.Node(connection)
        output = device.enable('show ip route')
  #      pprint(output)
        
        list = output[0]['result']['vrfs']['default']['routes']
        for route,type in list.items():
            route_addr = route
            route_type = type['routeType']
            if route_type == 'static':
                list2 = type['vias']
                for item in list2:
                    next_hop = item['nexthopAddr']
                print('{:^20}{:^20}{:^20}'.format(route_addr,route_type,next_hop))
            else:
                print('{:^20}{:^20}'.format(route_addr,route_type))       

 #pprint(list)
        
if __name__ == '__main__':
    main()
        
