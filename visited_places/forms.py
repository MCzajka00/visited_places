from flask_wtf import Form
from wtforms.fields.html5 import URLField
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, url


class BookmarkForm(Form):
    url = URLField('The URL with information about the place:', validators=[DataRequired(), url()])
    continent = StringField('Add continent where the place is located: ')
    country = StringField('Add country of place: ')
    city = StringField('Add name of place: ')


class LoginForm(Form):
    username = StringField('Your username:', validators=[DataRequired()])
    password = PasswordField('Password:', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log in')
