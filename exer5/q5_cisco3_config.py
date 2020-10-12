from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment (undefined = StrictUndefined)
env.loader = FileSystemLoader('.')

filename = 'q5_cisco3_config.j2'

my_var = {
    'timezone' : 'PST',
    'timezone_offset' : '-8 0',
    'timezone_dst' : 'PDT',
    'server1' : '130.126.24.24',
    'server2' : '152.2.21.1',
    }

template  = env.get_template(filename)
out = template.render(**my_var)
print(out)
