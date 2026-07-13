import functools

import flask

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
def visitors():
    return flask.render_template(
        'visitors.jinja',
        title='Visitor Log',
        heading="Visitor Log",
        content="Enter your visit details below.",
    )

@pages.route('/login', methods=['GET', 'POST'])
def login():

    return flask.render_template(
        'login.jinja',
        title='Login',
        heading="Login",
        content="Please enter your login details.",
    )


@pages.route('/logout', methods=['GET', 'POST'])
def logout():

    return flask.render_template(
        'logout.jinja',
        title='Logout',
        heading="Logout",
        content="Are you sure you want to log out?",
    )


@pages.route('/register', methods=['GET', 'POST'])
def register():

    return flask.render_template(
        'register.jinja',
        title='Register',
        heading="Register",
        content="Please fill in the form below to create an account.",
    )


if __name__ == '__main__':
    app.register_blueprint(pages)
    app.run()