import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

basedir = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'bm.login'


def create_app():
    visited_places_app = Flask(__name__)
    visited_places_app.config["SECRET_KEY"] = b'\x82\x8a\\\xb5\xbcd\x96\xb1\xb7das\x10e\x1b\x03'
    visited_places_app.config['DEBUG'] = True
    visited_places_app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'visited_places.db')}"

    from visited_places.views.default_views import main_bp
    from visited_places.views2 import bp

    visited_places_app.register_blueprint(main_bp)
    visited_places_app.register_blueprint(bp)

    db.init_app(visited_places_app)
    login_manager.init_app(visited_places_app)

    return visited_places_app


app = create_app()
