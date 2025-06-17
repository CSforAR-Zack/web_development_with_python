import flask


app = flask.Flask(__name__)


pages = flask.Blueprint(
    'pages',
    __name__,
    template_folder='templates',
    static_folder='static',
)


@pages.route('/')
def index():
    return flask.render_template(
        "index.html",
        title="Home",
    )


@pages.route('/countdown')
def countdown():
    return flask.render_template(
        "countdown.jinja",
        title="Countdown",
        time_left=10,
    )


@pages.route('/scrambler')
def scrambler():
    return flask.render_template(
        "scrambler.jinja",
        title="Scrambler",
    )


if __name__ == '__main__':
    app.register_blueprint(pages)
    app.run()