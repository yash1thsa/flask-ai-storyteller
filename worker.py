from celery import Celery
from app import create_app, db
from app.models import Story
import requests

celery = Celery(
    "worker",
    broker="redis://localhost:6379/0",  # assuming Redis
    backend="redis://localhost:6379/0"
)

@celery.task(bind=True)
def generate_story(self, child_name, favorite_character, setting, theme):
    try:
        response = requests.post(
            "http://127.0.0.1:11434/api/generate",
            json={
                "model": "mistral",
                "prompt": f"Write a short kids story about {favorite_character} in a {setting} with the theme of {theme}.",
                "stream": False
            }
        )
        story_text = response.json()["response"]

        app = create_app()
        with app.app_context():
            story = Story.query.filter_by(task_id=self.request.id).first()
            if story:
                story.story_text = story_text
                story.status = "completed"
                db.session.commit()
    except Exception as e:
        app = create_app()
        with app.app_context():
            story = Story.query.filter_by(task_id=self.request.id).first()
            if story:
                story.status = "failed"
                story.story_text = str(e)
                db.session.commit()
