import flask as fk

import todo.forms as tf
import todo.services as ts


pages = fk.Blueprint("pages", __name__, template_folder="templates")


@pages.route("/")
def index():
    """Render the index page."""
    return fk.render_template(
        "index.jinja",
        heading="Welcome to the TODO App",
        content="This is a simple TODO application built with Flask.",
    )

# Authentication routes
@pages.route("/login", methods=["GET", "POST"])
def login():
    """Render the login page."""
    form = tf.LoginForm()

    return fk.render_template(
        "login.jinja",
        title="Login",
        heading="Login to the TODO App",
        content="Please enter your credentials to log in.",
        form=form
    )


@pages.route("/logout", methods=["GET", "POST"])
def logout():
    """Render the logout page."""
    form = tf.LogoutForm()
    
    return fk.render_template(
        "logout.jinja",
        title="Logout",
        heading="Logout from the TODO App",
        content="Are you sure you want to log out?",
        form=form
    )

# Task management routes
@pages.route("/tasks", methods=["GET", "POST"])
def tasks():
    """Render the tasks page."""

    todo_list = ts.read_tasks_from_csv("todo/temp_tasks.csv")

    return fk.render_template(
        "tasks.jinja",
        title="Tasks",
        heading="Manage Your Tasks",
        content="Add, edit, and delete your tasks.",
        tasks=todo_list
    )


@pages.route("/done", methods=["GET", "POST"])
def done():
    """Render the done page."""
    
    completed_tasks = []

    return fk.render_template(
        "done.jinja",
        title="Done",
        heading="Completed Tasks",
        content="Here are the tasks you've completed.",
        tasks=completed_tasks,
    )