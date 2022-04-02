import os
from flask import Flask
from flask import render_template


template_dir = os. path. abspath('templates')
app = Flask(__name__, template_folder=template_dir)

@app.route('/')
def index():
    #return 'My first flask!'

    return render_template('index.html')

@app.route('https://anidurg.github.io/learngitacode/Hello/<name>')
def hello_name(name):
    return 'Hello ' +name

app.run(host='0.0.0.0', port=8080)
