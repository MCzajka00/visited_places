import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy()


def create_app():
    visited_places_app = Flask(__name__)
    visited_places_app.config["SECRET_KEY"] = b'\x82\x8a\\\xb5\xbcd\x96\xb1\xb7das\x10e\x1b\x03'
    visited_places_app.config['DEBUG'] = True
    visited_places_app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'visited_places.db')}"
    from visited_places.views import bp

    visited_places_app.register_blueprint(bp)
    db.init_app(visited_places_app)
    return visited_places_app


app = create_app()
