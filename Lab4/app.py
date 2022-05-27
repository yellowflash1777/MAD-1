from flask import Flask, render_template, request
import matplotlib
matplotlib.use('Agg')
from statistics import mean
import csv
import matplotlib.pyplot as plt
from jinja2 import Template


#reading data
file = open(r"data.csv")
reader=csv.DictReader(file,skipinitialspace=True)
data=list()
for i in reader:
    data.append(dict(i))
file.close()





app=Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
    if request.method=="GET":
        return render_template("index.html")
    elif request.method=="POST":
        ID=request.form["ID"]
        value=request.form["id_value"]
        if not ID or not value:
            return render_template("inv.html")

        elif ID=="course_id":
            course_marks=list()
            for i in data:
                
                if i["Course id"]==value:
                    course_marks.append(int(i["Marks"]))
            if len(course_marks)==0:
                    return render_template("inv.html")

   
            marks={'avg':mean(course_marks),'max':max(course_marks)}
            plt.clf()
            plt.hist(course_marks)
            plt.savefig('static\saved.png') 

            template_file=open("templates\course.html")
            TEMPLATE=template_file.read()
            template_file.close()

            template=Template(TEMPLATE)
            context=template.render(Marks=marks)

            new_html=open("templates\output.html",'w')
            new_html.write(context)
            new_html.close()

            return render_template("output.html")
        else:
                new_data=list()
                for i in data:
        
                    if i["Student id"]==value:
                        new_data.append(i)
                if len(new_data)==0:
                     return render_template("inv.html")

                temp=list()
                for i in new_data:
                    temp.append(int(i["Marks"]))
                total_marks=sum(temp)


                template_file=open("templates\student.html")
                TEMPLATE=template_file.read()
                template_file.close()

                template=Template(TEMPLATE)
                context=template.render(data=new_data,Total_Marks=total_marks)

                new_html=open("templates\output.html",'w')
                new_html.write(context)
                new_html.close()

                return render_template("output.html")
    else :
        return render_template("inv.html")


if __name__=="__main__":
    app.debug=True
    app.run()