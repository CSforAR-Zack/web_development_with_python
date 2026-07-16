import flask as fk
import flask_login as fkl

import todo.forms as tf
import todo.services as ts
import todo.models as tm


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

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        if ts.verify_user(username, password):
            user = ts.get_user_by_username(username)
            fkl.login_user(user)
            return fk.redirect(fk.url_for("pages.tasks"))
        else:
            fk.flash("Invalid username or password.", "error")

    return fk.render_template(
        "login.jinja",
        title="Login",
        heading="Login to the TODO App",
        content="Please enter your credentials to log in.",
        form=form
    )


@pages.route("/logout", methods=["GET", "POST"])
@fkl.login_required
def logout():
    """Render the logout page."""
    form = tf.LogoutForm()

    if form.validate_on_submit():
        if form.confirm_submit.data:
            fk.session.clear()
            fkl.logout_user()
            fk.flash("You have been logged out.", "success")
            return fk.redirect(fk.url_for("pages.index"))
        elif form.cancel_submit.data:
            return fk.redirect(fk.url_for("pages.tasks"))
    
    return fk.render_template(
        "logout.jinja",
        title="Logout",
        heading="Logout from the TODO App",
        content="Are you sure you want to log out?",
        form=form
    )


@pages.route("/create_account", methods=["GET", "POST"])
def create_account():
    """Render the account creation page."""
    form = tf.RegisterForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = ts.get_user_by_username(username)

        if user is None:
            ts.create_user(username, password)
            fk.flash("Account created successfully. Please log in.", "success")
            return fk.redirect(fk.url_for("pages.login"))
        else:
            fk.flash("There was a problem with that username and password!", "error")

    return fk.render_template(
        "create_account.jinja",
        title="Create Account",
        heading="Create a New Account",
        content="Please fill out the form below to create a new account.",
        form=form
    )


# Task management routes
@pages.route("/tasks", methods=["GET", "POST"])
@fkl.login_required
def tasks():
    """Render the tasks page."""
    form = tf.TaskForm()

    # Fetch tasks for the logged-in user
    task_list = ts.get_tasks_for_user(fkl.current_user.id)

    if form.validate_on_submit():
        return fk.redirect(fk.url_for("pages.task_add"))

    return fk.render_template(
        "tasks.jinja",
        title="Tasks",
        heading="Manage Your Tasks",
        content="Add, edit, and delete your tasks.",
        tasks=task_list,
        form=form,
    )


@pages.route("/task_add", methods=["GET", "POST"])
@fkl.login_required
def task_add():
    """Render the add task page."""
    form = tf.AddTaskForm()

    if form.validate_on_submit():
        task = tm.Task(
            title=form.title.data,
            description=form.description.data,
            user_id=fkl.current_user.id
        )
        ts.add_task(task)
        fk.flash("Task added successfully.", "success")
        return fk.redirect(fk.url_for("pages.tasks"))

    return fk.render_template(
        "task_add.jinja",
        title="Add Task",
        heading="Add a New Task",
        content="Fill out the form below to add a new task.",
        form=form
    )


@pages.route("/tasks_deleted", methods=["GET", "POST"])
@fkl.login_required
def tasks_deleted():
    """Render the deleted tasks page."""
    
    archived_tasks = ts.get_deleted_tasks_for_user(fkl.current_user.id)

    return fk.render_template(
        "tasks_deleted.jinja",
        title="Deleted Tasks",
        heading="Deleted Tasks",
        content="Here are the tasks you've deleted.",
        tasks=archived_tasks,
    )


@pages.route("/task/<int:task_id>/toggle", methods=["POST", "GET"])
@fkl.login_required
def task_toggle_complete(task_id):
    """Toggle a task's completion status."""
    task = ts.get_task(task_id, fkl.current_user.id)
    if task is None:
        fk.abort(404)

    task.completed = not task.completed
    ts.update_task(task)

    fk.flash("Task status updated.", "success")
    return fk.redirect(fk.url_for("pages.tasks"))


@pages.route("/task/<int:task_id>/edit", methods=["POST", "GET"])
@fkl.login_required
def task_edit(task_id):
    """Edit a task."""
    task = ts.get_task(task_id, fkl.current_user.id)
    if task is None:
        fk.abort(404)

    form = tf.EditTaskForm(obj=task)

    if form.validate_on_submit():
        task.title = form.title.data
        task.description = form.description.data
        ts.update_task(task)
        fk.flash("Task updated successfully.", "success")
        return fk.redirect(fk.url_for("pages.tasks"))

    return fk.render_template(
        "task_edit.jinja",
        title="Edit Task",
        heading="Edit Task",
        content="Modify the details of your task below.",
        form=form,
        task=task,
    )


@pages.route("/task/<int:task_id>/delete", methods=["POST", "GET"])
@fkl.login_required
def task_delete(task_id):
    """Delete a task."""
    task = ts.get_task(task_id, fkl.current_user.id)
    if task is None:
        fk.abort(404)

    ts.delete_task(task)
    fk.flash("Task deleted successfully.", "success")
    return fk.redirect(fk.url_for("pages.tasks_deleted"))


@pages.route("/task/<int:task_id>/toggle_delete", methods=["POST", "GET"])
@fkl.login_required
def task_toggle_delete_flag(task_id):
    """Toggle a task's deleted status."""
    task = ts.get_task(task_id, fkl.current_user.id)
    if task is None:
        fk.abort(404)

    task.deleted = not task.deleted
    ts.update_task(task)
    fk.flash("Task delete status updated.", "success")
    return fk.redirect(fk.url_for("pages.tasks"))
