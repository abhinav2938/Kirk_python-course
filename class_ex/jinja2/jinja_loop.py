from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined = StrictUndefined)
env.loader = FileSystemLoader('.')

my_var = {}

my_file = 'loop_cond.j2'
template = env.get_template(my_file)
output = template.render(**my_var)

print(output)
