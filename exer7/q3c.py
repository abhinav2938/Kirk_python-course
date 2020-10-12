from lxml import etree
import xmltodict
from pprint import pprint

def read_file(filename):    
    with open(filename, 'r') as f:
        file = f.read()
    xml_dict = xmltodict.parse(file, force_list = {'zones-security':True})
    return xml_dict

file1 = read_file('show_sec_zones.xml')
file2 = read_file('show_sec_z_s_t.xml')

pprint(file1)
pprint(file2)

print(type(file1['zones-information']['zones-security']))
print(type(file2['zones-information']['zones-security']))

