from flask import Blueprint, flash, url_for, render_template, redirect, abort, request
from flask_login import login_required, current_user

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

        bm = Bookmark(user=current_user, url=url, continent=continent, country=country, city=city)
        db.session.add(bm)
        db.session.commit()

        flash(f"Stored {city}")
        return redirect(url_for('user.user', username=current_user.username))
    return render_template('add.html', form=form)


@bm_bp.route('/delete/<int:bookmark_id>', methods=['GET', 'POST'])
@login_required
def delete_bookmark(bookmark_id):
    bookmark = Bookmark.query.get_or_404(bookmark_id)

    if current_user != bookmark.user:
        abort(403)

    if request.method == 'POST':
        db.session.delete(bookmark)
        db.session.commit()

        flash(f"Deleted {bookmark.city}")
        return redirect(url_for('user.user', username=current_user.username))
    else:
        flash("Please confirm deleting the bookmark.")
    return render_template('confirm_delete.html', bookmark=bookmark)

