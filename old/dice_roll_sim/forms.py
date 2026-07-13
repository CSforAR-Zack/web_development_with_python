from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField


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


class LogicGateForm(FlaskForm):
    toggle_left = SubmitField('False')
    operator = SelectField(
        'Operator',
        choices=[('AND', 'AND'), ('OR', 'OR'), ('XOR', 'XOR')],
        default='AND'
    )
    toggle_right = SubmitField('False')