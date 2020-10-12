from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined = StrictUndefined)
env.loader = FileSystemLoader('.')

base_intf = 'GigabitEthernet0/0/'
intf_list = []
for intf in range(25):
    intf = f"{base_intf}{intf}"
    intf_list.append(intf)
#print(intf_list)


#can be used to run only the above part for verification
#import sys
#sys.exit()

my_var = {'intf_list' : intf_list}

my_file = 'loops.j2'
template = env.get_template(my_file)
output = template.render(**my_var)

print(output)
