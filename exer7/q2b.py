from lxml import etree
import xmltodict
from pprint import pprint

with open('show_sec_zones.xml', 'r') as f:
    my_xml = f.read()
xml_dict = xmltodict.parse(my_xml)

req = xml_dict['zones-information']['zones-security']

#pprint(req)
for counter,value in enumerate(req,1):
    print ('Security Zone #{}: {}'.format(counter,value['zones-security-zonename']))
 
    
