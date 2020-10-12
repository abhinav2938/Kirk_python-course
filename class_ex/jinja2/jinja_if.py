from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

#env = Environment()
env = Environment(undefined = StrictUndefined)
env.loader = FileSystemLoader('.')
#env.loader = FileSystemLoader(['.', './templates/'])

my_var = {'primary_ip' : True}

my_file = 'intf_conf.j2'
temp = env.get_template(my_file)
out = temp.render(**my_var)

print(out)

