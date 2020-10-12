from jinja2.environment import Environment
from jinja2 import FileSystemLoader, StrictUndefined
from pprint import pprint

env = Environment(undefined = StrictUndefined)
env.loader = FileSystemLoader('.')

filename = 'q4.j2'

vrf1 = {
    'name' : 'blue',
    'number' : '100:1',
    'ipv4_enabled' : True,
    'ipv6_enabled' : False,
}
vrf2 = {
    'name' : 'blue2',
    'number' : '1001:1',
    'ipv4_enabled' : True,
    'ipv6_enabled' : True,
}
vrf3 = {
    'name' : 'blue3',
    'number' : '1002:1',
    'ipv4_enabled' : True,
    'ipv6_enabled' : False,
}
vrf4 = {
    'name' : 'blue4',
    'number' : '1003:1',
    'ipv4_enabled' : True,
    'ipv6_enabled' : True,
}
vrf5 = {
    'name' : 'blue5',
    'number' : '1004:1',
    'ipv4_enabled' : True,
    'ipv6_enabled' : False,
}
vrf_list = [vrf1, vrf2, vrf3, vrf4, vrf5]
#pprint(vrf_list)
#import sys
#sys.exit()

my_var = { 'vrf_list' : vrf_list}
template = env.get_template(filename)
out = template.render(**my_var)
print(out)
