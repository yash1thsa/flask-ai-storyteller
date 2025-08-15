from flask import Blueprint, render_template, request, redirect, url_for
from datetime import datetime
from app import db
from app.models import Story
from worker import generate_story

bp = Blueprint("main", __name__)

@bp.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        child_name = request.form["child_name"]
        favorite_character = request.form["favorite_character"]
        setting = request.form["setting"]
        theme = request.form["theme"]

        # enqueue Celery task
        task = generate_story.delay(child_name, favorite_character, setting, theme)

        # store in DB
        new_story = Story(
            child_name=child_name,
            favorite_character=favorite_character,
            setting=setting,
            theme=theme,
            story_text=None,
            task_id=task.id,
            status="pending",
            created_at=datetime.utcnow()
        )
        db.session.add(new_story)
        db.session.commit()

        return redirect(url_for("main.story_detail", story_id=new_story.id))

    return render_template("index.html")


@bp.route("/story/<int:story_id>")
def story_detail(story_id):
    story = Story.query.get_or_404(story_id)
    return render_template("story.html", story=story)
