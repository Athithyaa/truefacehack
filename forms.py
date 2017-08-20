from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, EqualTo, Length

# Set your classes here.


class HomeForm(Form):
    name = StringField('YouTube Link', [DataRequired()])

class PosterForm(Form):
    name = StringField('Poster Link', [DataRequired()])
