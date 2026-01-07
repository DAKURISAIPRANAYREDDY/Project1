from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config["SECRET_KEY"] = "your_secret_key"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    # Import routes and register blueprints
    from .routes import main
    app.register_blueprint(main)

    from .api import api_bp
    app.register_blueprint(api_bp, url_prefix="/api")

    # Create database if it doesn't exist
    with app.app_context():
        db.create_all()

    return app
