import functools

import flask
import passlib.hash as ph

import database as db
import forms


app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

pages = flask.Blueprint(
    'pages',
    __name__,
    template_folder='templates',
    static_folder='static',
)


def login_required(route):
    """Decorator to check if user is logged in."""
    @functools.wraps(route)
    def decorated_function(*args, **kwargs):
        if 'email' not in flask.session:
            flask.flash('You need to log in first.', 'error')
            return flask.redirect(flask.url_for('pages.login'))
        return route(*args, **kwargs)
    return decorated_function


# Error handling
@app.errorhandler(404)
def page_not_found(e):
    return flask.render_template(
        'error_404.jinja',
        title='Page Not Found',
        heading="Oops! Page Not Found",
        content="Try again later, or go back to the <a href='/'>home page</a>.",
    ), 404


@pages.route('/')
def index():
    return flask.render_template(
        'index.html',
        title='Welcome!',
        heading="Welcome, Visitor!",
        content="This is the home page for our museum visitor log application.",
    )


@pages.route('/visitors', methods=['GET', 'POST'])
@login_required
def visitors():
    form = forms.EntryForm()
    if form.validate_on_submit():
        db.enter_comment(form.name.data, form.date.data, form.reason.data)
        return flask.redirect(flask.url_for('pages.visitors'))

    visitors = db.get_comments()

    if visitors:
        visitors = [
            {
                'name': visitor[1],
                'date': visitor[2],
                'comment': visitor[3],
            }
            for visitor in visitors
        ]

        visitors.sort(key=lambda x: x['date'], reverse=True)
    return flask.render_template(
        'visitors.jinja',
        title='Visitor Log',
        heading="Visitor Log",
        content="Enter your visit details below.",
        form=form,
        visitors=visitors,
    )

@pages.route('/login', methods=['GET', 'POST'])
def login():
    form = forms.LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        if check_login(email, password):
            flask.session['email'] = email
            return flask.redirect(flask.url_for('pages.visitors'))
        else:
            flask.flash('Invalid email or password.', 'error')

    return flask.render_template(
        'login.jinja',
        title='Login',
        heading="Login",
        content="Please enter your login details.",
        form=form,
    )


@pages.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    form = forms.LogoutForm()
    if form.is_submitted():
        if form.confirm_submit.data:
            flask.session.pop('email', None)
            return flask.redirect(flask.url_for('pages.index'))
        elif form.cancel_submit.data:
            return flask.redirect(flask.url_for('pages.visitors'))

    return flask.render_template(
        'logout.jinja',
        title='Logout',
        heading="Logout",
        content="Are you sure you want to log out?",
        form=form,
    )


@pages.route('/register', methods=['GET', 'POST'])
def register():
    form = forms.RegisterForm()
    if form.validate_on_submit():
        email = form.email.data
        if db.get_user(email):
            flask.flash('Email already registered. Please log in.', 'error')
            return flask.redirect(flask.url_for('pages.login'))
        password = form.password.data
        password = ph.pbkdf2_sha256.hash(password)
        db.add_user(email, password)
        flask.flash('Registration successful! You can now log in.', 'success')
        return flask.redirect(flask.url_for('pages.login'))

    return flask.render_template(
        'register.jinja',
        title='Register',
        heading="Register",
        content="Please fill in the form below to create an account.",
        form=form,
    )


# Helper Functions
def check_login(email, password):
    user = db.get_user(email)
    if user and ph.pbkdf2_sha256.verify(password, user[2]):
        return True
    return False



if __name__ == '__main__':
    app.register_blueprint(pages)
    app.run(debug=True, host='0.0.0.0')