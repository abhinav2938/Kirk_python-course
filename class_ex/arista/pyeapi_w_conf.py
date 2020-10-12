import pyeapi

device1 = pyeapi.connect_to('arista7')
device2 = pyeapi.connect_to('arista8')
print(device1) 
print(device2) 
