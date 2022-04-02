import os
from flask import Flask
from flask import render_template


template_dir = os. path. abspath('templates')
app = Flask(__name__, template_folder=template_dir)

@app.route('/')
def index():
    #return 'My first flask!'

    return render_template('index.html')

@app.route('/Hello/<name>')
def hello_name(name):
    return 'Hello ' +name
