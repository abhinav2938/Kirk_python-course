from lxml import etree

a = '''
<zones-information>
    <zones-security>
        <zones-security-zonename>trust</zones-security-zonename>
        <zones-security-send-reset>Off</zones-security-send-reset>
        <zones-security-policy-configurable>Yes</zones-security-policy-configurable>
        <zones-security-interfaces-bound>1</zones-security-interfaces-bound>
        <zones-security-interfaces>
            <zones-security-interface-name>vlan.0</zones-security-interface-name>
        </zones-security-interfaces>
    </zones-security>
    <zones-security>
        <zones-security-zonename>untrust</zones-security-zonename>
        <zones-security-send-reset>Off</zones-security-send-reset>
        <zones-security-policy-configurable>Yes</zones-security-policy-configurable>
        <zones-security-screen>untrust-screen</zones-security-screen>
        <zones-security-interfaces-bound>2</zones-security-interfaces-bound>
        <zones-security-interfaces>
            <zones-security-interface-name>fe-0/0/0.0</zones-security-interface-name>
            <zones-security-interface-name>pt-1/0/0.0</zones-security-interface-name>
        </zones-security-interfaces>
    </zones-security>
    <zones-security>
        <zones-security-zonename>junos-host</zones-security-zonename>
        <zones-security-send-reset>Off</zones-security-send-reset>
        <zones-security-policy-configurable>Yes</zones-security-policy-configurable>
        <zones-security-interfaces-bound>0</zones-security-interfaces-bound>
        <zones-security-interfaces>
        </zones-security-interfaces>
    </zones-security>
</zones-information>
'''

my_xml = etree.fromstring(a)
print(my_xml.tag)
print(my_xml.getchildren())
print(my_xml.getchildren()[0])
print(my_xml.getchildren()[0].tag)
print(len(my_xml))
#q 1e
trust_zone = my_xml[0]
print(f'trust_zone: {trust_zone}')
print(f'printing the text of the element: {trust_zone[0].text}')

#q 1f
#for child in my_xml.getchildren().iterdescendants():
for child in trust_zone:
    print(child.tag)
#print(etree.tostring(my_xml).decode())

    
