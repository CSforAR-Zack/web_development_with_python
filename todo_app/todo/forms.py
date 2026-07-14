import flask_wtf as f_wtf # What The Form...
import wtforms as wtf


class LoginForm(f_wtf.FlaskForm):
    email = wtf.StringField(
        'email',
        render_kw={'placeholder': 'EMAIL'},
        validators=[wtf.validators.DataRequired(), wtf.validators.Email()],
    )
    password = wtf.PasswordField(
        'password',
        render_kw={'placeholder': 'PASSWORD'},
        validators=[wtf.validators.DataRequired()],
    )
    submit = wtf.SubmitField('Login')


class LogoutForm(f_wtf.FlaskForm):
    confirm_submit = wtf.SubmitField('Confirm')
    cancel_submit = wtf.SubmitField('Cancel')