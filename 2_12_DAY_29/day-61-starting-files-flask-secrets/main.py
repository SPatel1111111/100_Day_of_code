from flask import Flask, render_template,request,redirect,url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired

app = Flask(__name__)
app.secret_key = 'this-is-my-secret-key'

class LoginForm(FlaskForm):
    email = StringField('Email',[InputRequired()])
    password = PasswordField('Password',[InputRequired()])

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login",methods=['GET','POST'])
def login():
    email= None
    password =None
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            email=form.email.data
            password=form.password.data
            if email=='sneha.patel1@aliansoftware.com' and password=='1234567':
                return redirect(url_for("success"))
            else:
                return redirect(url_for('denied'))
    else:
        return render_template('login.html', form=form,email=email,password=password)

@app.route("/denied")
def denied():
    return render_template('denied.html')

@app.route("/success")
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
