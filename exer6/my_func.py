import yaml


def read_yaml():
    with open('q2.yml') as f:
        device = f.read()
        return(yaml.load(device))
    raise ValueError('reading yaml failed')

def output_print(list1):
    #list1 = output[0]['result']['ipV4Neighbors']
        for arp in list1:
            ip_add = arp['address']
            mac_add = arp['hwAddress']
            print('{:^15} ---> {:^15}'.format(ip_add,mac_add))
