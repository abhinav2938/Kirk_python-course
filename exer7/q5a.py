from lxml import etree
from pprint import pprint

#read using rb mode as it includes encoding information
with open('show_version.xml', 'rb') as f:
    file = f.read()

my_xml = etree.fromstring(file)
print(my_xml.nsmap)
#print(my_xml)

#5b
#a = my_xml.find('.//{*}proc_board_id')
#print(a.text)

