import yaml

filename = input('enter the filename: \n')
with open(filename) as f:
    yaml_out = yaml.load(f)
print()
print(yaml_out)
