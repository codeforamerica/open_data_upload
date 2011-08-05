"""
Flask Documentation:       http://flask.pocoo.org/docs/
Jinja2 Documentation:      http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:    http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""

from flask import Flask

import settings
from views import views
from models import db


def create_app():
    """Create your application."""
    app = Flask(__name__)
    app.config.from_object(settings)
    app.register_module(views)
    db.app = app
    db.init_app(app)
    db.create_all()
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
