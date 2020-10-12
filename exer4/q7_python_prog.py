import textfsm
from pprint import pprint

template_fl = 'q2_sh_int_status.tpl'
template = open(template_fl)

with open('q1_sh_int_status.txt') as f:
    raw_text = f.read()

re_table = textfsm.TextFSM(template)
data = re_table.ParseText(raw_text)
template.close()
my_list = []
header = re_table.header

for item in data:
    x = zip(header,item)
    x = dict(x)
    my_list.append(x)
pprint(my_list)

#pprint(re_table.header)
#print('Output data: \n')
#pprint(data)

