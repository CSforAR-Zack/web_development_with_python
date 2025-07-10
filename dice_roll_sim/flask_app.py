import random
import json

import flask
import plotly
import plotly.express as px
import pandas as pd

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


@pages.route('/dice', methods=['GET', 'POST'])
def dice():
    form: forms.DiceForm = forms.DiceForm()
    figure = None  # Initialize figure to None

    if form.validate_on_submit():
        # Get the number of sides for each die and the number of rolls
        die1_sides = int(form.die1.data)
        die2_sides = int(form.die2.data)
        rolls = int(form.rolls.data)

        # Create figures based on the dice roll simulation
        figure = create_dice_graph(die1_sides, die2_sides, rolls)

    return flask.render_template(
        'dice.jinja',
        title='Dice Sim',
        heading="Dice Simulation",
        content="Enter your dice roll details below.",
        form=form,
        figure=figure,
    )


def create_dice_graph(die1_sides, die2_sides, rolls):
    # Roll the dice, sum sides, determine frequency
    results: list = []

    for roll in range(rolls):
        die1 = random.randint(1, die1_sides)
        die2 = random.randint(1, die2_sides)
        result: int = die1 + die2
        results.append(result)
        
    counts: dict = {}
    max_result: int = die1_sides + die2_sides

    for sum_value in range(2, max_result + 1):
        counts[sum_value] = results.count(sum_value)

    # Create a bar chart using Plotly
    x = list(counts.keys())
    y = list(counts.values())

    df = pd.DataFrame({'Sum of Dice': x, 'Frequency': y})

    fig = px.bar(
        df,
        x='Sum of Dice',
        y='Frequency',
        labels={'x': 'Sum of Dice', 'y': 'Frequency'},
        title=f'Dice Roll Simulation: {rolls} Rolls of {die1_sides}-sided and {die2_sides}-sided Dice',
        color='Frequency',
        height=800,
        template="plotly_dark",
        color_continuous_scale='Viridis'
    )

    graph_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return graph_json


if __name__ == '__main__':
    app.register_blueprint(pages)
    app.run()