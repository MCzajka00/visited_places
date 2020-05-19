from flask import Flask, render_template, redirect, url_for, flash, Blueprint

from visited_places.forms import BookmarkForm

bp = Blueprint('bm', __name__, url_prefix="/")
bookmarks = [
    {
        "user": "Tom",
        "url": "https://en.wikivoyage.org/wiki/Karlsruhe",
        "continent": "Europe",
        "country": "Deutschland",
        "city": "Karlsruhe"
    },
    {
        "user": "Katie",
        "url": "https://en.wikivoyage.org/wiki/Split",
        "continent": "Europe",
        "country": "Croatia",
        "city": "Split"
    },
    {
        "user": "Anna",
        "url": "https://en.wikivoyage.org/wiki/Vienna",
        "continent": "Europe",
        "country": "Austria",
        "city": "Vienna"
    }
]


def get_latest_place(limit):
    return bookmarks[:limit]


@bp.route("/")
@bp.route("/index")
def index():
    return render_template("index.html", bookmarks=get_latest_place(5))


@bp.route("/add", methods=['GET', 'POST'])
def add():
    form = BookmarkForm()

    if form.validate_on_submit():
        url = form.url.data
        continent = form.continent.data
        country = form.country.data
        city = form.city.data

        bm = {
            "user": "Magda",
            "url": url,
            "continent": continent,
            "country": country,
            "city": city
        }

        bookmarks.append(bm)
        flash(f"Stored {city}")
        return redirect(url_for('index'))
    return render_template('add.html', form=form)


@bp.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@bp.errorhandler(500)
def server_error(e):
    return render_template("500.html"), 500
