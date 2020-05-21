from flask import flash, request, url_for, render_template, redirect, Blueprint
from flask_login import login_user

from visited_places.forms import LoginForm
from visited_places.models import User

user_bp = Blueprint("user", __name__, url_prefix="/users")


@user_bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.get_by_username(form.username.data)
        if user is not None and user.check_password(form.password.data):
            login_user(user, form.remember_me.data)
            flash(f"Logged in successfully as {user.username}")
            return redirect(request.args.get('next') or url_for('main.index'))
        flash(f"Incorrect username or password")
    return render_template('login.html', form=form)
