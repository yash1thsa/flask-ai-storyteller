from flask import Blueprint, request, render_template, jsonify
from app.services import generate_story
from app.models import Story
from app import db

main = Blueprint("main", __name__)


@main.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        data = request.form
        story_text = generate_story(data["child_name"], data["favorite_character"], data["setting"], data["theme"])

        new_story = Story(child_name=data["child_name"], story_text=story_text)
        db.session.add(new_story)
        db.session.commit()

        return render_template("story.html", story=story_text)

    return render_template("index.html")