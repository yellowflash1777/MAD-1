from re import template
from jinja2 import Template
import csv
import sys

first_arg=sys.argv[0]
second_arg=sys.argv[1]

file = open(r"data.csv")
reader=csv.DictReader(file)
data=list()
for i in reader:
    data.append(dict(i))
file.close()

temp=list()
for i in data:
    temp.append(int(i[" Marks"]))

total_marks=sum(temp)


template_file=open(r"base.html")
TEMPLATE=template_file.read()
template_file.close()

template=Template(TEMPLATE)
context=template.render(data=data,Total_Marks=total_marks)

new_html=open("output.html",'w')
new_html.write(context)
new_html.close()