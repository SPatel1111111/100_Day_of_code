# from jinja2 import Template
#
# name='jinja'
# email='jinja@gmail.com'
# n=[1,2,3,4,5,6,7,8,9]
#
# file =open('index1.html','r')
# content =file.read()
# file.close()
#
# template =Template(content)
# render_form=template.render(t_name=name,t_email=email,even=n)
#
#
# output=open('index.html','w')
# output.write(render_form)
# output.close()
from flask import Flask,render_template

app = Flask(__name__)
@app.route('/')
def video():
    message= "Video Route"
    return render_template("video.html",message=message)

if __name__=='__main__':
    app.run(debug=True)
