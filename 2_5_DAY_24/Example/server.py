# decorator: it is design pattern which modify the functionality of function by wrapped it in another function.
#jinja: it is  templating language (dynamic html pages with it like logic perform in python)
from flask import Flask, render_template
import random
import datetime
import requests
import json

app = Flask(__name__)

@app.route('/')
def hello():
    random_num = random.randint(0, 10)
    current_year = datetime.datetime.now().year
    return render_template("index.html", number=random_num, y=current_year)

@app.route('/guess/<uname>')
def guess(uname):
    age_url = f"https://api.agify.io?name={uname}"
    age_response = requests.get(age_url)
    data1 = age_response.json()
    age1 = data1["age"]

    gender_url = f"https://api.genderize.io?name={uname}"
    gender_response = requests.get(gender_url)
    data2 = gender_response.json()
    gender1 = data2["gender"]

    return render_template("guess.html", name=uname, gender=gender1, age=age1)

#docs:https://www.npoint.io/docs/929cbb599a79101b2d6f
@app.route('/blog/<num>')
def get_blog(num):
    blog_url = "https://api.npoint.io/929cbb599a79101b2d6f"
    blog_response = requests.get(blog_url)
    all_post= blog_response.json()

    return render_template("blog.html",posts=all_post)


if __name__ == "__main__":
    app.run(debug=True)
