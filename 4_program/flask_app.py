import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/about')
def about():
    return flask.render_template('about.html')

@app.route('/hobby')
def hobby():
    return flask.render_template('hobby.html')

@app.route('/work')
def work():
    return flask.render_template('work.html')
