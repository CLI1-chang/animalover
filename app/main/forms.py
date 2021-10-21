from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class NameForm(FlaskForm):
    name = StringField('Please tell us your name', validators=[DataRequired()])
    submit = SubmitField('Submit')
