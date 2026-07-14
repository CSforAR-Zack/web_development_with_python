import pathlib as pl

import flask as fk

from todo.routes import pages


def create_app():
    """Create and configure the Flask application. This
    is a factory pattern that allows us to create multiple
    instances of the app with different configurations."""
    
    # Create the Flask application instance
    app = fk.Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY="dev",  # Change this in production
        DATABASE="sqlite:///todo.db",  # Database URI
    )

    # Check if /instance folder exists, if not create it
    pl.Path(app.instance_path).mkdir(exist_ok=True)

    # Register the blueprints
    app.register_blueprint(pages)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()