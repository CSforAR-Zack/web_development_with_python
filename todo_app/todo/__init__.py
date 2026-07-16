import flask as fk

import todo.routes as tr
import todo.extensions as te
import todo.services as ts


def create_app():
    """Create and configure the Flask application. This
    is a factory pattern that allows us to create multiple
    instances of the app with different configurations."""
    
    # Create the Flask application instance
    app = fk.Flask(__name__)
    app.config["SECRET_KEY"] = "dev"  # Change this in production
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
    
    # Initialize the extensions
    te.db.init_app(app)
    te.csrf.init_app(app)
    te.login_manager.init_app(app)

    te.login_manager.login_view = "pages.login"
    te.login_manager.login_message_category = "error"

    @te.login_manager.user_loader
    def load_user(user_id):
        return ts.get_user_by_id(int(user_id))

    # Register the blueprints
    app.register_blueprint(tr.pages)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()