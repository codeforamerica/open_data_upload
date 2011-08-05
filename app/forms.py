"""
WTForms Documentation:    http://wtforms.simplecodes.com/
Flask WTForms Patterns:   http://flask.pocoo.org/docs/patterns/wtforms/
Flask-WTF Documentation:  http://packages.python.org/Flask-WTF/

Forms for your application can be stored in this file.
"""

from flaskext.wtf import (Form, SubmitField, TextField, FileField,
                          TextAreaField, Required, Email)


class UploadForm(Form):
    """A simple form for uploading files to Open Data Boston."""
    name = TextField('Name', validators=[Required()])
    email = TextField('Email', validators=[Email()])
    phone = TextField('Phone Number')
    file = FileField()
    title = TextField('Title')
    url = TextField('Dataset URL')
    description = TextAreaField('Description', validators=[Required()])
    submit = SubmitField('Submit')
