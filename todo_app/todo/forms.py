import flask_wtf as f_wtf # What The Form...
import wtforms as wtf


class LoginForm(f_wtf.FlaskForm):
    username = wtf.StringField(
        'username',
        render_kw={'placeholder': 'USERNAME'},
        validators=[wtf.validators.DataRequired()],
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


class TaskForm(f_wtf.FlaskForm):
    submit = wtf.SubmitField('Add Task')


class AddTaskForm(f_wtf.FlaskForm):
    title = wtf.StringField(
        'Title',
        render_kw={'placeholder': 'Task Title'},
        validators=[wtf.validators.DataRequired()],
    )
    description = wtf.TextAreaField(
        'Description',
        render_kw={'placeholder': 'Task Description'},
        validators=[wtf.validators.DataRequired()],
    )
    submit = wtf.SubmitField('Add Task')
    cancel = wtf.SubmitField('Cancel')


class EditTaskForm(f_wtf.FlaskForm):
    title = wtf.StringField(
        'Title',
        render_kw={'placeholder': 'Task Title'},
        validators=[wtf.validators.DataRequired()],
    )
    description = wtf.TextAreaField(
        'Description',
        render_kw={'placeholder': 'Task Description'},
        validators=[wtf.validators.DataRequired()],
    )
    submit = wtf.SubmitField('Update Task')
    cancel = wtf.SubmitField('Cancel')