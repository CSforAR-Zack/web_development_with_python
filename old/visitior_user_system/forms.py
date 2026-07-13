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


class LoginForm(FlaskForm):
    email = StringField(
        'email',
        render_kw={'placeholder': 'EMAIL'},
        validators=[validators.DataRequired(), validators.Email()],
    )
    password = StringField(
        'password',
        render_kw={'placeholder': 'PASSWORD'},
        validators=[validators.DataRequired()],
    )
    submit = SubmitField('Login')


class LogoutForm(FlaskForm):
    confirm_submit = SubmitField('Confirm')
    cancel_submit = SubmitField('Cancel')


class RegisterForm(FlaskForm):
    email = StringField(
        'email',
        render_kw={'placeholder': 'EMAIL'},
        validators=[validators.DataRequired(), validators.Email(), validators.Length(min=6, max=35)],
    )
    password = StringField(
        'password',
        render_kw={'placeholder': 'PASSWORD'},
        validators=[validators.DataRequired(), validators.Length(min=6, max=35)],
    )
    submit = SubmitField('Register')
