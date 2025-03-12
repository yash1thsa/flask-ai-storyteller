from app import db
from datetime import datetime

class Story(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique ID
    child_name = db.Column(db.String(50), nullable=False)  # Child's name
    favorite_character = db.Column(db.String(100), nullable=False)  # Favorite character
    setting = db.Column(db.String(100), nullable=False)  # Story setting
    theme = db.Column(db.String(100), nullable=False)  # Theme
    story_text = db.Column(db.Text, nullable=False)  # Generated story
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Timestamp

    def __repr__(self):
        return f"<Story {self.child_name} - {self.created_at}>"

# Example User Model (if authentication is needed)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"<User {self.username}>"