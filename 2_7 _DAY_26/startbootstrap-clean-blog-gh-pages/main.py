from flask import Flask, render_template
import requests

app = Flask(__name__)

blog_url = "https://api.npoint.io/929cbb599a79101b2d6f"
blog_response = requests.get(blog_url)
all_post = blog_response.json()
@app.route('/about.html')
def about():
    return render_template("about.html")

@app.route('/')
def home():
    return render_template("index.html",posts=all_post)

@app.route('/contact.html')
def contact():
    return render_template("contact.html")

@app.route('/post.html')
def first_post():
    return render_template("post.html")
@app.route('/post/<int:num>')
def find_post(num):
    requested_post = None
    for blog_post in all_post:
        if int(blog_post["id"]) == num:
            requested_post=blog_post

    return render_template("post1.html",posts=requested_post)

if __name__ == "__main__":
    app.run(debug=True)
