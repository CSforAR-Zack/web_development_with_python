import flask_wtf as fw
import wtforms as wt

class EntryForm(fw.FlaskForm):
    name = wt.StringField(
        'Visitor',
        render_kw={'placeholder': 'Enter your name'},
        validators=[wt.validators.DataRequired()],
    )
    date = wt.DateField(
        'Date of Visit',
        format='%Y-%m-%d',
        render_kw={'placeholder': 'YYYY-MM-DD'},
        validators=[wt.validators.DataRequired()],
    )
    reason = wt.TextAreaField(
        'Reason for Visit',
        render_kw={'placeholder': 'Enter the reason for your visit'},
        validators=[wt.validators.DataRequired()],
    )
    submit = wt.SubmitField('Submit')


class LoginForm(fw.FlaskForm):
    email = wt.StringField(
        'email',
        render_kw={'placeholder': 'EMAIL'},
        validators=[wt.validators.DataRequired(), wt.validators.Email()],
    )
    password = wt.StringField(
        'password',
        render_kw={'placeholder': 'PASSWORD'},
        validators=[wt.validators.DataRequired()],
    )
    submit = wt.SubmitField('Login')


class LogoutForm(fw.FlaskForm):
    confirm_submit = wt.SubmitField('Confirm')
    cancel_submit = wt.SubmitField('Cancel')


class RegisterForm(fw.FlaskForm):
    email = wt.StringField(
        'email',
        render_kw={'placeholder': 'EMAIL'},
        validators=[wt.validators.DataRequired(), wt.validators.Email(), wt.validators.Length(min=6, max=35)],
    )
    password = wt.StringField(
        'password',
        render_kw={'placeholder': 'PASSWORD'},
        validators=[wt.validators.DataRequired(), wt.validators.Length(min=6, max=35)],
    )
    submit = wt.SubmitField('Register')
