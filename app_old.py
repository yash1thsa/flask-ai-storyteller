from flask import Flask, render_template, request, jsonify
import requests
import pyttsx3

app = Flask(__name__)

# DeepSeek API Endpoint & Key
DEEPSEEK_API_URL = "https://api.deepseek.com/v1/chat/completions"
DEEPSEEK_API_KEY = "sk-2915c7a29c224ede8479585fd70e1ab3"  # Replace with your API key


def generate_story(child_name, favorite_character, setting, theme):
    """Generate a personalized bedtime story using DeepSeek API"""
    prompt = f"Write a short bedtime story for an 8-year-old named {child_name}. Include {favorite_character} in a magical {setting}. The theme should be {theme}."

    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "deepseek-chat",  # Adjust model name if needed
        "messages": [{"role": "system", "content": "You are a bedtime story generator."},
                     {"role": "user", "content": prompt}],
        "temperature": 0.7
    }

    response = requests.post(DEEPSEEK_API_URL, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return "Error: Unable to generate story." + str(response.status_code)


# def read_story_aloud(story_text):
#     """Convert story text to speech"""
#     engine = pyttsx3.init()
#     engine.say(story_text)
#     engine.runAndWait()


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # Get form data
        child_name = request.form["child_name"]
        favorite_character = request.form["favorite_character"]
        setting = request.form["setting"]
        theme = request.form["theme"]

        # Generate the story
        story = generate_story(child_name, favorite_character, setting, theme)

        return render_template("index.html", story=story, child_name=child_name)

    return render_template("index.html", story=None)


if __name__ == "__main__":
    app.run(debug=True)
