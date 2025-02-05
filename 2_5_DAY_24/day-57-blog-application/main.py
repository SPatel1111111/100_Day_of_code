from flask import Flask, render_template
import requests

app = Flask(__name__)

blog_url = "https://api.npoint.io/929cbb599a79101b2d6f"
# @app.route('/')
# def home():
#     return render_template("index.html")

@app.route('/')
def get_blog():
    blog_response = requests.get(blog_url)
    all_post = blog_response.json()

    return render_template("index.html",posts=all_post)

@app.route('/post/<int:num>')
def find_post(num):
    blog_response = requests.get(blog_url)
    all_post = blog_response.json()

    if num == 1:
        return render_template("post.html",posts=all_post)
    if num == 2:
        return render_template("post2.html",posts=all_post)
    if num == 3:
        return render_template("post3.html",posts=all_post)

if __name__ == "__main__":
    app.run(debug=True)
