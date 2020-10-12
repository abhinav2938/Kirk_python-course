from lxml import etree

with open ('show_sec_zones.xml', 'r') as f:
    file = f.read()

my_xml = etree.fromstring(file)
#print(my_xml.tag)
#a = my_xml.find('zones-security')
#print('Find tag of the first zones-security element')
#print('-'*30)
#print(a.tag)
#print()
#
#ch = a.getchildren()
#print('Find tag of all child elements of the first zones-security element')
#print('-'*30)
#for child in ch:
#    print(child.tag)

#q4b
#a= my_xml.getchildren()[0]
#print(a)
#new = a.find('zones-security-zonename')
#print(new)
#print(new.text)

#q4c
a = my_xml.findall('zones-security')
for element in a:
  #  print(element)
    new = element.find('zones-security-zonename')
    print(new, new.text)
  #  print(element.text)

#print(a)


#txt = print(a.text)

