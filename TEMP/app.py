from jinja2 import Template
from flask import Flask,render_template,request,redirect
import sqlite3
import os

app=Flask(__name__)

#currentlocation=os.path.dirname(os.path.dirpath(__file))
@app.route("/listform",methods=['GET','POST'])
def listform():
    if request.method=='POST':
        lname=request.form['name']
        desc=request.form['desc']
        name=username
        print(lname,desc,name)
        sqlconnection=sqlite3.Connection('newdb.sqlite3')
        cursor=sqlconnection.cursor()

        query1="insert into LISTS(NAME,DESC,USERNAME) values ('{}','{}','{}')".format(lname,desc,name)
        #print(query1)
        cursor.execute(query1)
        sqlconnection.commit()
        cursor.close()
        return redirect('/kanban')
    else:
        return render_template("listform.html")

@app.route("/kanban")
def kanban():
    return render_template("kanban.html")

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/signup",methods=['GET','POST'])
def signup():
    if request.method=="POST":
        
        un=request.form.get('username')
        pw=request.form.get('password')
        #print(un,pw)
        sqlconnection=sqlite3.Connection('newdb.sqlite3')
        cursor=sqlconnection.cursor()

        query1="insert into users(username,password) values ('{}','{}')".format(un,pw)
        #print(query1)
        cursor.execute(query1)
        sqlconnection.commit()
        cursor.close()

        return redirect('/')

    return render_template("signup.html")

@app.route("/login_validation",methods=['POST'])
def login_validation():
    global username
    username=request.form.get('username')
    password=request.form.get('password')

    sqlconnection=sqlite3.Connection('newdb.sqlite3')
    cursor=sqlconnection.cursor()
    #print(username,password)
    query0='SELECT username,password from users'

    query1="SELECT username,password from users where username='{}' and password='{}'".format(username,password)
    #print(query1)
    rows=cursor.execute(query1)
    rows=rows.fetchall()
    cursor.close()
    if len(rows)==1:
        return render_template('home.html',name=username),username
    else:
        return redirect('/')

    
    return rows

if __name__=="__main__":
    app.debug=True
    app.run()