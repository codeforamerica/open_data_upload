"""
Flask Module Docs:  http://flask.pocoo.org/docs/api/#flask.Module

This file is used for both the routing and logic of your
application.
"""

import os
from flask import Module, render_template, request, redirect, url_for
from werkzeug import secure_filename

from forms import UploadForm
from settings import UPLOAD_FOLDER

views = Module(__name__, 'views')


@views.route('/')
def index():
    """Render website's index page."""
    return redirect(url_for('upload'))


@views.route('/upload/', methods=('GET', 'POST'))
def upload():
    """Render the website's about page."""
    form = UploadForm()
    if request.method == 'POST' and form.validate_on_submit():
        data_file = request.files['file']
        file_name = secure_filename(data_file.filename)
        data_file.save(os.path.join(UPLOAD_FOLDER, file_name))
        return redirect(url_for('thanks'))
    return render_template('upload.html', form=form)


@views.route('/thanks/')
def thanks():
    return render_template('thanks.html')


# The functions below should be applicable to all Flask apps.

@views.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return views.send_static_file(file_dot_text)


@views.route('/qunit/')
def qunit():
    """Render a QUnit page for JavaScript tests."""
    return render_template('test_js.html')


@views.after_request
def add_header(response):
    """Add header to force latest IE rendering engine and Chrome Frame."""
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    return response


@views.app_errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
