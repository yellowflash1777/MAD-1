from imghdr import what
from flask import Flask, redirect, request, url_for
from flask import render_template
from flask import current_app as app
from numpy import who
from .database import db
from application.models import  Course, Enrollments, Student

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
            return render_template("error.html",who='Student',what='Roll No',where='')
        else:
            course = Course.query.filter_by(course_id=courseid).first()
            student = Student(roll_number=roll_number, first_name=first_name, last_name=last_name)
            student.courses.append(course)
            db.session.add(student)        
            db.session.commit()
            return redirect(url_for("home"))
    return render_template("create_student.html")

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

@app.route("/student/<rollno>/delete", methods=["GET"])
def delete_student(rollno):
    student = Student.query.filter_by(roll_number=rollno).first()
    db.session.delete(student)
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/student/<rollno>", methods=["GET"])
def student_details(rollno):
    student = Student.query.filter_by(roll_number=rollno).first()
    return render_template("student_details.html", student=student ,len=len(student.courses))

@app.route("/student/<student_id>/withdraw/<course_id>")
def withdraw(student_id,course_id):
    enrollment=Enrollments.query.filter_by(student_id=student_id,course_id=course_id).first()
    db.session.delete(enrollment)
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/course")
def course():
    courses=Course.query.all()
    return render_template("courses.html",course=courses)

@app.route("/course/create", methods=["GET", "POST"])
def course_create():
    if request.method == "POST":               
        course_code = request.form.get("code")
        course_name = request.form.get("c_name")
        course_description = request.form.get("desc")        
        course=Course.query.filter_by(course_code=course_code).first()
        if course:
            return render_template("error.html",who='Course',what='Course code',where='course')
        else:
            course=Course(course_code=course_code,course_name=course_name,course_description=course_description)
            db.session.add(course)        
            db.session.commit()
            return redirect(url_for("course"))
    return render_template("create_course.html")

@app.route("/course/<courseid>/update", methods=["GET", "POST"])
def update_course(courseid):
    if request.method == "POST":
        course_name = request.form.get("c_name")
        course_description = request.form.get("desc")
        
        course = Course.query.filter_by(course_id=courseid).first()
        course.course_name=course_name
        course.course_description=course_description    
    
        db.session.commit()
        return redirect(url_for("course"))
    course = Course.query.filter_by(course_id=courseid).first()
    
    return render_template("update_course.html", course=course)