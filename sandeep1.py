from flask import Flask,render_template  
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('web2.html')
'''if _name__== '__main__':
    app.run(debug = True)
'''

app.run()
