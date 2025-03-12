from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import config

db = SQLAlchemy()


def create_app(env="development"):
    app = Flask(__name__)
    app.config.from_object(config[env])

    db.init_app(app)
    CORS(app)

    from app.routes import main
    app.register_blueprint(main)

    return app