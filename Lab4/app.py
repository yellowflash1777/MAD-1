
from http.client import HTTPResponse
from flask import Flask, request
from flask import render_template



app=Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("helo.html")

@app.route("/post", methods=["GET","POST"])
def demo_post():
    if request.method=="GET":
     return render_template("post.html")
    elif request.method=="POST":
        username=request.form["username"]
        return render_template("after.html",username=username)
    else:
        return HTTPResponse("nope")

if __name__=='__main__':
    app.debug=True
    app.run()