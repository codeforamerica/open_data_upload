"""
You can store your app's configuration settings here.

Generate good secret keys:  http://flask.pocoo.org/docs/quickstart/#sessions
    >>> import os
    >>> os.urandom(24)
    '\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8'
"""

import os


def current_location(name):
    """Find the current upload folder for data."""
    if os.path.exists('/home/dotcloud/current'):
        upload_folder = '/home/dotcloud/' + name
    else:
        upload_folder = os.path.join(os.getcwd(), name)
    return upload_folder


SQLALCHEMY_DATABASE_URI = 'sqlite:///' + current_location('test.db')
SQLALCHEMY_ECHO = False
SECRET_KEY = "this_is_my_secret_key_that_I_should_change_with_os.urandom"
UPLOAD_FOLDER = current_location('open_data')
