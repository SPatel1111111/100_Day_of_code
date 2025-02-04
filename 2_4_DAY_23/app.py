#udemy day55
from flask import Flask
import random as r
app=Flask(__name__)

print(r.__name__)
print(__name__)
@app.route('/')
def hello_world():
    return '<h1 style="text-align:center">hello,world!!</h1>'\
            '<p> this is paragraph</p>'\
            '<img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExaGhkYzdvZHBibjFidGt3cHF1NjhqMXd4MzczbmYwNGc2emJzcXo4OCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/LOYX1OVNPK9sQ/giphy.gif"; width=300>'

def make_em(func):
    def warp_em():
        return f'<em>{func()}</em>'
    return warp_em
def make_b(func):
    def warp_b():
        return f'<b>{func()}</b>'
    return warp_b
def make_u(func):
    def warp_u():
        return f'<u>{func()}</u>'
    return warp_u
@app.route('/bye')
@make_em
@make_u
@make_b
def bye():
    return "hey bye!!"

# @app.route('/<path:name>')
# @app.route('/<name>/1')
@app.route('/<name>/<int:number>')
def greet(name,number):
    return f" hello there !! {name},you are {number}year old."

if __name__== "__main__":
    app.run(debug=True)