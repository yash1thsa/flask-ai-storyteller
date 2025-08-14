from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .config import config  # adjust import path

db = SQLAlchemy()

def create_app(env_name):
    app = Flask(__name__)
    app.config.from_object(config[env_name])

    # Import & register blueprints here
    from .routes import main
    app.register_blueprint(main)

    # Initialize extensions here
    from .models import db
    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.config.update(
        CELERY_BROKER_URL='redis://localhost:6379/0',
        CELERY_RESULT_BACKEND='redis://localhost:6379/0'
    )
    from .celery_app import celery
    celery.conf.update(app.config)

    return app
