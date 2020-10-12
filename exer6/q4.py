from getpass import getpass
from jinja2.environment import Environment
from jinja2 import FileSystemLoader, StrictUndefined
import yaml
import pyeapi
import time
from pprint import pprint

def load_yaml():
    with open('q4_arista.yml', 'r') as f:
        return(yaml.load(f))
    raise ValueError('reading yaml failed')


def main():
#if __name__ == '__main__':
    env = Environment(undefined = StrictUndefined)
    env.loader = FileSystemLoader('.')
    password = getpass()
    filename = 'q4.j2'

    device = load_yaml()
    #pprint('device: {}'.format(device))
    #import sys
    #sys.exit()
    for name,device_dict in device.items():
        device_dict['password'] = password
        dict_value = ['username','transport','host','port','password']

        # need to separate the dictionary values, one for logging and other for the config command
        new_dict = {}
        intf_dict = {}
        for key,value in device_dict.items():
            if key in dict_value:
    #can also do new_dict[key] = device_dict[key]
                new_dict[key] = value
            else:
                intf_dict[key] = value
            #as the configuration values are in another dictionary with key= 'data'
            for k,v in intf_dict.items():
                intf_dict2 = v
        print('intf dict: {}'.format(intf_dict2)) 
        print('new_dict: {}'.format(new_dict))
        template = env.get_template(filename)
        output = template.render(**intf_dict2)
        #the format needs to be in list so used splitlines()
        out_list = output.splitlines()
        print('template configuration being send to {} : {}'.format(new_dict['host'],out_list))

        connection = pyeapi.client.connect(**new_dict)
        device = pyeapi.client.Node(connection)
        send_config = device.config(out_list)
        print('sending configuration to arista: {}'.format(send_config))
        
       # sleep_time = 5
       # print(f'sleeping for {sleep_time} seconds')
       # time.sleep(sleep_time)

        sh_cmd = device.enable('show ip interface brief')
        pprint('show command out: {}'.format(sh_cmd[0]['result']['output'].rstrip()))
        
if __name__ == '__main__':
   main()
