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
    form = forms.EntryForm()
    if form.validate_on_submit():
        db.enter_data(form.name.data, form.date.data, form.reason.data)
        return flask.redirect(flask.url_for('pages.visitors'))

    visitors = db.get_visitors()

    if visitors:
        visitors = [
            {
                'name': visitor[1],
                'date': visitor[2],
                'reason': visitor[3],
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



if __name__ == '__main__':
    app.register_blueprint(pages)
    app.run()
