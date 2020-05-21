from flask_wtf import Form
from wtforms.fields.html5 import URLField
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, url, Length, Regexp, EqualTo, Email, ValidationError

from visited_places.models import User


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


class SignUpForm(Form):
    username = StringField('Username:',
                           validators=[
                               DataRequired(),
                               Length(3, 80),
                               Regexp('^[A-Za-z0-9_]{3,}$',
                                      message='Username consist of number, letters and underscores.')
                           ])
    password = PasswordField('Password:',
                             validators=[
                                 DataRequired(),
                                 EqualTo('password2', message="Password must match")
                             ])
    password2 = PasswordField('Confirm password',
                              validators=[DataRequired()])
    email = StringField('Email:',
                        validators=[
                            DataRequired(),
                            Length(5, 120),
                            Email()
                        ])
    submit = SubmitField('Sign up')

    def validate_email(self, email_field):
        if User.query.filter_by(email=email_field.data).first():
            raise ValidationError('There is already user with this e-mail.')

    def validate_username(self, username_field):
        if User.query.filter_by(username=username_field.data).first():
            raise ValidationError('There username is already taken. Please choose something else.')

