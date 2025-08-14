import requests
from app.celery_app import celery
from time import sleep

OLLAMA_API_URL =  "http://127.0.0.1:11434/api/generate"

@celery.task(name="app.services.generate_story")
def generate_story(child_name, favorite_character, setting, theme):
    """
    Generate a personalized bedtime story using a local Ollama model.
    """
    prompt = (
        f"Write a bedtime infant story for {child_name} featuring {favorite_character} "
        f"in {setting} with a {theme} theme."
    )

    # Ollama expects `model` and `prompt` in JSON
    data = {
        "model": "mistral",  # change to your preferred local model
        "prompt": prompt,
        "stream": False  # return the entire output at once
    }
    sleep(5)
    response = requests.post(OLLAMA_API_URL, json=data)

    if response.status_code == 200:
        return response.json().get("response", "")
    else:
        return f"Error generating story: {response.text}"
