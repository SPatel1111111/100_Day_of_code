from flask import Flask
import random as r
app=Flask(__name__)

print(r.__name__)
print(__name__)
@app.route('/')
def hello_world():
    return "hello,world!!"

@app.route('/bye')
def bye():
    return "hey bye!!"

if __name__== "__main__":
    app.run()