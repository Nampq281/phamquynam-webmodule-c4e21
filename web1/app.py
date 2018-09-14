#1. Create a flask app
from flask import Flask, render_template

app = Flask(__name__)
ps = [
    "I. Most academic writing tasks require you to make an argument—that is, to present reasons for a particular claim or interpretation you are putting forward. You may have been told that you need to make your arguments more logical or stronger. And you may have worried that you simply aren’t a logical person or wondered what it means for an argument to be strong. Learning to make the best arguments you can is an ongoing process, but it isn’t impossible: “Being logical” is something anyone can do, with practice.",
    "II. Each argument you make is composed of premises (this is a term for statements that express your reasons or evidence) that are arranged in the right way to support your conclusion (the main claim or interpretation you are offering). You can make your arguments stronger ",
    "III. It is particularly easy to slip up and commit a fallacy when you have strong feelings about your topic—if a conclusion seems obvious to you, you’re more likely to just assume that it is true and to be careless with your evidence. To help you see how people commonly make this mistake, this handout uses a number of controversial political examples—arguments about subjects like abortion, gun control, the death penalty, gay marriage, euthanasia, and pornography."   
    ]
y = len(ps)
# 2. Create router
@app.route("/")
def homepage():
    return render_template("homepage.html", 
    posts=ps, 
    title="Homepage")

@app.route("/posts/<int:position>")
def post_no(position):
    if position < 0 or position >=len(ps):
        return "Not found", 404
    post= ps[position-1]
    return render_template("post_detail.html",
    post= post)

@app.route("/posts")
def posts(): 
    cut_ps = []
    for post in ps:
        cut_ps.appened(post[0:40])
    return render_template("post_list.html",
    posts=ps)

@app.route("/nam")
def hello_nam():
    return "Hello Nam"

@app.route("/hello/<name>")
def hello(name):
    return "Hello " + name

@app.route("/add/<int:x>/<int:y>")
def add_no(x,y):
    z = x + y
    return str(z)

@app.route("/h1tag")
def h1tag():
    return "<h1>Heading 1 - Biggggggg</h1><p>Lop C4E</p>"
#3. Run app
print("Running app")
if __name__ == "__main__":
    app.run(debug=True) # listening
