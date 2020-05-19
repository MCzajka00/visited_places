from flask import Flask, render_template, redirect, url_for, flash, Blueprint

from visited_places import db
from visited_places.forms import BookmarkForm
from visited_places.models import Bookmark

bp = Blueprint('bm', __name__, url_prefix="/")


@bp.route("/")
@bp.route("/index")
def index():
    return render_template("index.html", bookmarks=Bookmark.latest(5))


@bp.route("/add", methods=['GET', 'POST'])
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


@bp.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@bp.errorhandler(500)
def server_error(e):
    return render_template("500.html"), 500
