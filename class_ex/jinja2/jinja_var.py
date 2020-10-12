from jinja2 import Template

text1 = '''
hi what's up {{bgp_as}}
abhinav here {{random_ip}}
more {{bgp_id}}
'''

text2 = '''
some math
will come soon here {{34+6}}
be hold {{9*0}}
'''

my_dict = {
        'bgp_as' : '2234',
        'bgp_id' : '2.3.4.6',
        'random_ip' : '1.1.1.1'
    }

tmp1 = Template(text1)
out = tmp1.render(**my_dict)
print(out)
