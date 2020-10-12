import json
from pprint import pprint

filename = 'test.json'
with open(filename, 'r') as f:
    data = json.load(f)

print()
pprint(data)
print()
