Value Port_no (\S+)
Value Vlan (\d)
Value Speed (\S+)


Start
  ^Port .* Type -> ip_int

ip_int
  ^${Port_no}\s+\S+\s+${Vlan}\s+\S+\s+${Speed}\s+\S+$$ -> Record

EOF
 



#Port      Name  Status       Vlan  Duplex Speed Type 
#Gi0/1/0         notconnect   1     auto   auto  10/100/1000BaseTX
#Gi0/1/1         notconnect   1     auto   auto  10/100/1000BaseTX
#Gi0/1/2         notconnect   1     auto   auto  10/100/1000BaseTX
#Gi0/1/3         notconnect   1     auto   auto  10/100/1000BaseTX
