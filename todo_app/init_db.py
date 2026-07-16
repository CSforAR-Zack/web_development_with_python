from todo import create_app
from todo.extensions import db
import todo.models as tm
import todo.services as ts


app = create_app()
with app.app_context():
    db.drop_all() # Drop all existing tables and data in the database

    db.create_all()

    # Create a new user
    user = ts.create_user("admin", "pass")
    db.session.add(user)
    db.session.commit()
