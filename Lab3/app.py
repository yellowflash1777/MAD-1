from audioop import avgpp
from re import template
from jinja2 import Template
import csv
import sys
from statistics import mean
import matplotlib.pyplot as plt

first_arg=sys.argv[1]
second_arg=sys.argv[2]

file = open(r"data.csv")
reader=csv.DictReader(file,skipinitialspace=True)
data=list()
for i in reader:
    data.append(dict(i))
file.close()

if first_arg=='-s':
    new_data=list()
    for i in data:
        
        if i["Student id"]==second_arg:
            new_data.append(i)

    temp=list()
    for i in new_data:
        temp.append(int(i["Marks"]))
    total_marks=sum(temp)


    template_file=open(r"student_base.html")
    TEMPLATE=template_file.read()
    template_file.close()

    template=Template(TEMPLATE)
    context=template.render(data=new_data,Total_Marks=total_marks)




else:
    course_marks=list()
    for i in data:
        if i["Course id"]==second_arg:
            course_marks.append(int(i["Marks"]))

   
    marks={'avg':mean(course_marks),'max':max(course_marks)}
    plt.hist(marks)

    template_file=open(r"course_base.html")
    TEMPLATE=template_file.read()
    template_file.close()

    template=Template(TEMPLATE)
    context=template.render(Marks=marks)
    

  


new_html=open("output.html",'w')
new_html.write(context)
new_html.close()
