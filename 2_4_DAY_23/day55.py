# class User:
#     def __init__(self,name):
#         self.name =name
#         self.is_logged_in = False
#
# def is_authenticated_decorator(func):
#     def wrapper(*arg,**kwargs):
#         if arg[0].is_logged_in == True:
#             func(arg[0])
#     return wrapper
# @is_authenticated_decorator
# def create_blog_post(user):
#     print(f"this is user {user.name}'s new blog.")
#
# new_user= User("me")
# new_user.is_logged_in=True
# create_blog_post(new_user)
#


#need to work on this
from flask import Flask
app = Flask(__name__)

class User:
    def __init__(self):
        self.is_logged_in = False

def make_bold(func):
    def wrapper(*args, **kwargs):
        user = kwargs.get('user')
        if user and user.is_logged_in:
            return f"<b>func(*args, **kwargs)</b>"
        return func(*args, **kwargs)

    return wrapper

new_user = User()
new_user.is_logged_in = True

@app.route('/bye')
@make_bold
def bye(user=new_user):
    return "hey bye!!"


if __name__ == "__main__":
    app.run(debug=True)
