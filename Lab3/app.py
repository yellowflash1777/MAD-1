from audioop import avgpp
from re import template
from jinja2 import Template
import csv
import sys
from statistics import mean
import matplotlib.pyplot as plt

first_arg=-1
second_arg=-1
if len(sys.argv)==3:
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




elif first_arg=='-c':
    course_marks=list()
    for i in data:
        if i["Course id"]==second_arg:
            course_marks.append(int(i["Marks"]))

   
    marks={'avg':mean(course_marks),'max':max(course_marks)}
    plt.hist(course_marks)
    plt.savefig('saved.jpeg') 

    template_file=open(r"course_base.html")
    TEMPLATE=template_file.read()
    template_file.close()

    template=Template(TEMPLATE)
    context=template.render(Marks=marks)

else:
    template_file=open(r"error_base.html")
    TEMPLATE=template_file.read()
    template_file.close()

    template=Template(TEMPLATE)
    context=template.render()   

    

  


new_html=open("output.html",'w')
new_html.write(context)
new_html.close()
