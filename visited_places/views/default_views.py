from flask import render_template, Blueprint

from visited_places import login_manager
from visited_places.models import Bookmark, User

main_bp = Blueprint("main", __name__, url_prefix="/")


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@main_bp.route("/")
@main_bp.route("/index")
def index():
    return render_template("index.html", bookmarks=Bookmark.latest(5))


@main_bp.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@main_bp.errorhandler(500)
def server_error(e):
    return render_template("500.html"), 500


@main_bp.errorhandler(403)
def forbidden(e):
    return "strona nie działa"
