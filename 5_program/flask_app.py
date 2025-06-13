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
        'index.html',
        title='Welcome!',
        heading="Welcome, Mortals, to My Humble Website!",
        content="Greetings, puny creatures, and welcome to the digital dwelling of Grog the Mighty! Tread lightly, for within these pages lie the chronicles of my magnificent existence. Feel free to click around, but try not to track too much mud onto my finely polished pixels.",
    )

@pages.route('/about')
def about():
    return flask.render_template(
        'about.jinja',
        title='About Me',
        heading="About Me",
        content="Once, a mere babe, now a hulking force of nature, I've traded raiding villages for competitive napping and occasional poetry slams.",
    )

@pages.route('/hobby')
def hobby():
    return flask.render_template(
        'hobby.jinja',
        title='Hobby',
        heading="My Hobby",
        content="My hobbies include meticulously organizing my collection of shiny human teeth and perfecting my guttural battle cry, which doubles as a surprisingly effective alarm clock.",
    )

@pages.route('/work')
def work():
    return flask.render_template(
        'work.jinja',
        title='Work',
        heading="My Work",
        content='Having retired from the glorious art of pillaging, I now proudly serve as a "motivational speaker" for goblin-run start-ups, mostly by grunting encouragement and occasional threats.',
    )


if __name__ == '__main__':
    app.register_blueprint(pages)
    app.run()
