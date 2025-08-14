from flask import Blueprint, render_template, request
from app import db
from app.models import Story
from app.services import generate_story

main = Blueprint("main", __name__)

@main.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        data = request.form
        story_text = generate_story.delay(
            data.get("child_name"),
            data.get("favorite_character"),
            data.get("setting"),
            data.get("theme")
        )

        new_story = Story(
            child_name=data.get("child_name"),
            favorite_character=data.get("favorite_character"),
            setting=data.get("setting"),
            theme=data.get("theme"),
            story_text=story_text
        )
        db.session.add(new_story)
        db.session.commit()

        return render_template("story.html", story=story_text)

    return render_template("index.html")