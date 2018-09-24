from flask import Flask, render_template, request
import mlab
from post import Post

app = Flask(__name__)
mlab.connect()

@app.route("/new-post", methods=["GET", "POST"])
def new_post():
    if request.method == "GET":
        return render_template("new_post.html")
    elif request.method == "POST":
        form = request.form
        t = form["title"]
        a = form["author"]
        c = form["content"]

    new_post = Post(title=t, author=a, content=c, likes=0)
    new_post.save()
    return "OK"


if __name__=="__main__":
    app.run(debug=True)
