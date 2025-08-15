from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.Config")

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Import and register routes AFTER db is initialized
    from app.routes import bp
    app.register_blueprint(bp)

    return app
