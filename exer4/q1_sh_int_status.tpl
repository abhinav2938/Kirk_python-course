Value PORT_NAME (\S+)
Value STATUS (\S+)
Value VLAN (\d+)
Value DUPLEX (.+)
Value SPEED (.+)
Value TYPE (\S+)


Start
  ^Port.* Type\s+ -> ShInt

ShInt
  ^${PORT_NAME}\s+${STATUS}\s+${VLAN}\s+${DUPLEX}\s+${SPEED}\s+${TYPE} -> Record

EOF 




#Port      Name  Status       Vlan  Duplex Speed Type 
#Gi0/1/0         notconnect   1     auto   auto  10/100/1000BaseTX
#Gi0/1/1         notconnect   1     auto   auto  10/100/1000BaseTX
#Gi0/1/2         notconnect   1     auto   auto  10/100/1000BaseTX
#Gi0/1/3         notconnect   1     auto   auto  10/100/1000BaseTX
