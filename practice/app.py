from flask import Flask, render_template, redirect, url_for, request
import mlab
from post import Post

app = Flask(__name__)
mlab.connect()

@app.route('/')
def homepage():
    return redirect(url_for('posts'))

@app.route('/post/<post_id>')
def post(post_id):
    post = Post.objects().with_id(post_id)
    if post is None:
        return "Not found"
    else:
        return render_template('post.html', post=post)

@app.route('/posts')
def posts():
    posts = Post.objects()
    return render_template('posts.html', posts=posts)

@app.route('/new-post', methods=["GET", "POST"])
def new_post():
    if request.method == "GET":
        return render_template('new-post.html')
    elif request.method == "POST":
        form = request.form 
        t = form["title"]          
        a = form["author"]
        c = form["content"]
        new_post = Post(title=t, author=a, content=c)
        new_post.save()
        return redirect(url_for('posts'))

@app.route('/delete/<post_id>')
def delete(post_id):
    post = Post.objects().with_id(post_id)
    post.delete()
    return redirect(url_for('posts'))
@app.route('/update/<post_id>', methods=['GET','POST'])
def update(post_id):
    post = Post.objects().with_id(post_id) 
    if request.method == 'GET':
        return render_template('update.html', post=post)
    elif request.method == 'POST':
        form = request.form 
        t = form['title']
        a = form['author']
        c = form['content']
        post.update(set__title=t, set__author=a, set__content=c)
    return redirect('/post/' +post_id)

if __name__ == "__main__":
    app.run(debug=True)