from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class DiceForm(FlaskForm):
    die1 = StringField(
        'Die 1', render_kw={'placeholder': 'Enter number of sides'}
    )
    die2 = StringField(
        'Die 2', render_kw={'placeholder': 'Enter number of sides'}
    )
    rolls = StringField(
        'Number of Rolls', render_kw={'placeholder': 'Enter number of rolls'}
    )
    submit = SubmitField('Roll Dice')
