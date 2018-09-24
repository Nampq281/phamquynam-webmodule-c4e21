from flask import Flask, render_template, redirect

app = Flask(__name__)
content = ["Name: Pham Quy Nam",
"Age: 24",
"Work: finance", 
"School: Techkid school",
"Hobbies: classic guitar, swimming, reading"
] 
@app.route("/")
def homepage ():
    return render_template("homepage.html", 
    title = "Homepage"
    )
@app.route("/aboutme")
def aboutme ():
    return render_template("about_me.html",
    posts = content,
    title = "About me"
    )
@app.route("/school")
def school ():
    return redirect("http://techkids.vn", code=302)
    
print("running app")
if __name__ == "__main__":
    app.run(debug=True)
