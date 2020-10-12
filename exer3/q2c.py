import yaml
from pprint import pprint



with open('file.yml', 'r')as f:
    y = yaml.load(f)

pprint(y)
