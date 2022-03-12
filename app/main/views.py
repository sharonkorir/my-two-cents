from flask import render_template
from . import main
from ..request import get_quote 
from flask_login import login_required

@main.route('/')
def index():
    title = 'My Two Cents'
    quote = get_quote()
    return render_template('index.html', title=title, quote=quote)

@main.route('/post/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_review(id):
    pass