#udemy day55
from flask import Flask
import random
main=Flask(__name__)

random_num=random.randint(0,9)
print(random_num)
@main.route('/')
def home():
    return "<h1 style='text-align:center'>guess a number between 0 to 9</h1>"\
        "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' style='vertical-align:middle;margin:0px 750px'>"

@main.route('/<int:guess>')
def guess(guess):
    if guess < random_num:
        return "<h2 style='text-align:center;color: purple'>Too low, try again!</h2>"\
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'style='vertical-align:middle;margin:0px 700px'>"
    elif guess == random_num:
        return "<h2 style='text-align:center;color: purple'>You found me!</h2>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' style='vertical-align:middle;margin:0px 800px' >"
    else:
        return "<h2 style='text-align:center;color: purple'>Too high, try again!</h2>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' style='vertical-align:middle;margin:0px 700px'>"

if __name__=="__main__":
    main.run(debug=True)
