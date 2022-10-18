from flask import Flask, redirect, request, url_for
from flask import render_template
from flask import current_app as app
from .database import db
from application.models import  Course, Student

@app.route("/", methods=["GET", "POST"])
def home():
    students = Student.query.all()
    return render_template("index.html",students=students)

@app.route("/student/create", methods=["GET", "POST"])
def student_create():
    if request.method == "POST":               
        roll_number = request.form.get("roll")
        first_name = request.form.get("f_name")
        last_name = request.form.get("l_name")
        courseid = request.form.get("courses")
        l=[]
        rollList=Student.query.with_entities(Student.roll_number).all()
        for i in range(len(rollList)):
            l.append(rollList[i][0])
        if roll_number in l:
            return render_template("error.html")
        else:
            course = Course.query.filter_by(course_id=courseid).first()
            student = Student(roll_number=roll_number, first_name=first_name, last_name=last_name)
            student.courses.append(course)
            db.session.add(student)        
            db.session.commit()
            return redirect(url_for("home"))
    return render_template("create_student.html")

@app.route("/articles_by/<user_name>", methods=["GET", "POST"])
def articles_by_author(user_name):
    articles = Article.query.filter(Article.authors.any(username=user_name))
    return render_template("articles_by_author.html", articles=articles, username=user_name)

@app.route("/student/<rollno>/update", methods=["GET", "POST"])
def update_student(rollno):
    if request.method == "POST":
        first_name = request.form.get("f_name")
        last_name = request.form.get("l_name")
        courseid = request.form.get("courses")
        course = Course.query.filter_by(course_id=courseid).all()
        student = Student.query.filter_by(roll_number=rollno).first()
        
        student.first_name = first_name
        student.last_name = last_name
        student.courses.extend(course)
        db.session.commit()
        return redirect(url_for("home"))
    student = Student.query.filter_by(roll_number=rollno).first()
    
    return render_template("update_student.html", student=student) 