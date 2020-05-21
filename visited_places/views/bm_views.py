from flask import Blueprint, flash, url_for, render_template, redirect
from flask_login import login_required

from visited_places import db
from visited_places.forms import BookmarkForm
from visited_places.models import Bookmark

bm_bp = Blueprint('bm', __name__, url_prefix="/bookmarks")


@bm_bp.route("/add", methods=['GET', 'POST'])
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
        return redirect(url_for('main.index'))
    return render_template('add.html', form=form)
