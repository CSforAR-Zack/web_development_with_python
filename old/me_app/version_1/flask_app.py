from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Welecome to my Me Application!"

@app.route('/about')
def about():
    return "This is the about page of my Me Application!"

@app.route('/hobby')
def hobby():
    return "My hobby is playing video games!"

@app.route('/work')
def work():
    return "I work as a computer science specialist!"
