from flask import render_template
from . import main

@main.route('/')
def index():
    message = 'Test'
    return render_template('index.html', message=message)

