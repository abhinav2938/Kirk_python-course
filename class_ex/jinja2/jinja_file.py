from jinja2 import Template

filename = 'bgp_config.j2'
with open(filename) as f:
    bgp_temp = f.read()

my_dict = {
    'bgp_as' : '65000',
    'router_id' : '2.3.4.5',
#    'peer1' : '25'
}

bgp_temp1 = Template(bgp_temp)
out = bgp_temp1.render(**my_dict)

print(out)

