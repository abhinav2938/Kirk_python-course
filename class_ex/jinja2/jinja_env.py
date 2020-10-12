#from __future__ import unicode_literals, print_function
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

#env = Environment()
env = Environment(undefined = StrictUndefined)
#env.loader = FileSystemLoader('.')
env.loader = FileSystemLoader(['.', './templates/'])

my_dict = {
    'bgp_as' : '65000',
    'router_id' : '2.3.4.5',
    'peer1' : '25'
}

my_file = 'bgp_config.j2'
temp = env.get_template(my_file)
out = temp.render(**my_dict)

print(out)

