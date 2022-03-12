from flask import render_template
from . import main
from ..request import get_quote 

@main.route('/')
def index():
    title = 'My Two Cents'
    quote = get_quote()
    return render_template('index.html', title=title, quote=quote)

