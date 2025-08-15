from datetime import datetime
from . import db

class Story(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    child_name = db.Column(db.String(50), nullable=False)
    favorite_character = db.Column(db.String(50), nullable=False)
    setting = db.Column(db.String(50), nullable=False)
    theme = db.Column(db.String(50), nullable=False)
    story_text = db.Column(db.Text, nullable=True)
    task_id = db.Column(db.String(50), nullable=True)
    status = db.Column(db.String(20), default="pending")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
