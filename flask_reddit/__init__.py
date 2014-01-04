#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Written by:
Lucas Ou-Yang -- http://codelucas.com
Jason Tanner -- http://jasontanner.herokuapp.com
"""
from flask import Flask, render_template, url_for
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__, static_url_path='/static/flask_reddit')
app.config.from_object('config')

db = SQLAlchemy(app)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

from flask_reddit.users.views import mod as users_module
app.register_blueprint(users_module)

from flask_reddit.threads.views import mod as threads_module
app.register_blueprint(threads_module)

@app.route('/')
def hello():
    return render_template('home.html')

def custom_render(template, *args, **kwargs):
    """
    custom template rendering including some flask_reddit vars
    """
    return render_template(template, *args, **kwargs)

app.debug = app.config['DEBUG']

if __name__ == '__main__':
    print 'We are running flask via main()'
    app.run()
