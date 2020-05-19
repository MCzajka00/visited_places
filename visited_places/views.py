from flask import Flask, render_template, redirect, url_for, flash, Blueprint, request
from flask_login import login_user, logout_user, current_user, login_required

from visited_places import db, login_manager
from visited_places.forms import BookmarkForm, LoginForm
from visited_places.models import Bookmark, User

bp = Blueprint('bm', __name__, url_prefix="/")


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@bp.route("/")
@bp.route("/index")
def index():
    return render_template("index.html", bookmarks=Bookmark.latest(5))


@bp.route("/add", methods=['GET', 'POST'])
@login_required
def add():
    form = BookmarkForm()

    if form.validate_on_submit():
        url = form.url.data
        continent = form.continent.data
        country = form.country.data
        city = form.city.data

        bm = Bookmark(url=url, continent=continent, country=country, city=city)
        db.session.add(bm)
        db.session.commit()

        flash(f"Stored {city}")
        return redirect(url_for('bm.index'))
    return render_template('add.html', form=form)


@bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.get_by_username(form.username.data)
        if user is not None and user.check_password(form.password.data):
            login_user(user, form.remember_me.data)
            flash(f"Logged in successfully as {user.username}")
            return redirect(request.args.get('next') or url_for('bm.index'))
        flash(f"Incorrect username or password")
    return render_template('login.html', form=form)


@bp.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@bp.errorhandler(500)
def server_error(e):
    return render_template("500.html"), 500
