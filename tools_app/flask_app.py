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


if __name__ == '__main__':
    app.register_blueprint(pages)
    app.run()