'''
from flask import Flask
app= Flask(__name__)
#home page , index page , landing page are the meaning of front slash.
@app.route('/hello/<name>')
def hello_name(name):
    return 'hello %s'%name
if __name__== '__main__':
    app.run(debug = True)

'''
from flask import Flask,render_template #redirct, url_for 
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('wbb.html')
if __name__== '__main__':
    app.run(debug = True)
