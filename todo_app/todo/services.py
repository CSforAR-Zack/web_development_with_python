import werkzeug.security as ws

import todo.models as tm


def create_user(username, password):
    """Create a new user with the given username and password."""
    password_hash = ws.generate_password_hash(password)
    new_user = tm.User(username=username, password=password_hash)
    return new_user


def verify_user(username, password):
    """Verify the user's credentials."""
    user: tm.User = tm.User.query.filter_by(username=username).first()
    if user and ws.check_password_hash(user.password, password):
        return True
    return False


def get_user_by_id(user_id):
    """Retrieve a user by their ID."""
    return tm.User.query.get(int(user_id))


def get_user_by_username(username):
    """Retrieve a user by their username."""
    return tm.User.query.filter_by(username=username).first()


def get_tasks_for_user(user_id):
    """Retrieve non-deleted tasks for a specific user."""
    return tm.Task.query.filter_by(user_id=user_id, deleted=False).all()


def get_deleted_tasks_for_user(user_id):
    """Retrieve deleted tasks for a specific user."""
    return tm.Task.query.filter_by(user_id=user_id, deleted=True).all()


def get_task(task_id):
    """Retrieve a task by its ID."""
    return tm.Task.query.get(int(task_id))


def add_task(task):
    """Add a new task to the database."""
    tm.db.session.add(task)
    tm.db.session.commit()


def update_task(task):
    """Update an existing task in the database."""
    tm.db.session.add(task)
    tm.db.session.commit()


def delete_task(task):
    """Delete a task from the database."""
    tm.db.session.delete(task)
    tm.db.session.commit()