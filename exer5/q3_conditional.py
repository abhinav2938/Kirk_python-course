from jinja2.environment import Environment
from jinja2 import FileSystemLoader, StrictUndefined

env = Environment(undefined = StrictUndefined)
env.loader = FileSystemLoader('.')

filename = 'q3.j2'

my_dict = {
    'name' : 'blue',
    'number' : '100:1',
    'ipv4_enabled' : True,
    'ipv6_enabled' : Falsee,
}

template = env.get_template(filename)
out = template.render(**my_dict)
print(out)
