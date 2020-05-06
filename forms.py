from flask_wtf import Form
from wtforms.fields.html5 import URLField
from wtforms import StringField
from wtforms.validators import DataRequired, url


class BookmarkForm(Form):
    url = URLField('The URL with information about the place:', validators=[DataRequired(), url()])
    continent = StringField('Add continent where the place is located: ')
    country = StringField('Add country of place: ')
    city = StringField('Add name of place: ')
