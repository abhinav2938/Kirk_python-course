Value Device_ID (\S+)
Value Local_Intf (\S+)
Value Capability (\w+)
Value Port_ID (\S+)

Start
  ^Device .* ID.* -> ShLLDP

ShLLDP
  ^${Device_ID}\s+${Local_Intf}\s+ \d+\s+${Capability}\s+${Port_ID}.* $$ -> Record




#Capability codes:
#  (R) Router, (B) Bridge, (T) Telephone, (C) DOCSIS Cable Device
#  (W) WLAN Access Point, (P) Repeater, (S) Station, (O) Other
#Device ID                         Local Intf          Hold-time   Capability  Port ID     
#nxos2.twb-tech.com                Eth2/1              120          BR          Eth2/1      
#nxos2.twb-tech.com                Eth2/2              120          BR          Eth2/2      
#nxos2.twb-tech.com                Eth2/3              120          BR          Eth2/3      
#nxos2.twb-tech.com                Eth2/4              120          BR          Eth2/4      
#Total entries displayed: 4
