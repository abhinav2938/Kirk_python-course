from lxml import etree
import xmltodict
from pprint import pprint

with open('show_sec_zones.xml', 'r') as f:
    my_xml = f.read()
#my_xml = etree.fromstring(my_xml)
#print(my_xml.tag)
xml_dict = xmltodict.parse(my_xml)
pprint(xml_dict)
print(f'The type is: {type(xml_dict)}')
