from re import template
from jinja2 import Template
import csv

file = open(r"data.csv")
reader=csv.DictReader(file)
data=list()
for i in reader:
    data.append(dict(i))
file.close()

template_file=open(r"base.html")
TEMPLATE=template_file.read()
template_file.close()

template=Template(TEMPLATE)
