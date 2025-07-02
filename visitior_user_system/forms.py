from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, DateField, validators

class EntryForm(FlaskForm):
    name = StringField(
        'Visitor',
        render_kw={'placeholder': 'Enter your name'},
        validators=[validators.DataRequired()],
    )
    date = DateField(
        'Date of Visit',
        format='%Y-%m-%d',
        render_kw={'placeholder': 'YYYY-MM-DD'},
        validators=[validators.DataRequired()],
    )
    reason = TextAreaField(
        'Reason for Visit',
        render_kw={'placeholder': 'Enter the reason for your visit'},
        validators=[validators.DataRequired()],
    )
    submit = SubmitField('Submit')