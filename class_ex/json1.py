import json

list1 = ['uncc','mit','rps','convent']
my_dict = {
        'name': 'abhi',
        'age': '25',
        'school': list1,
        'null_val': None,
        'bool_val': True
    }


filename = 'test.json'
with open(filename, 'wt') as f:
    json.dump(my_dict, f, indent = 4)

print()
print(my_dict)
print()
print(json.dumps(my_dict))
print()
