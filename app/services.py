import requests
import os

DEEPSEEK_API_URL = "https://api.deepseek.com/v1/chat/completions"
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")

def generate_story(child_name, favorite_character, setting, theme):
    """Generate a personalized bedtime story using DeepSeek API."""
    prompt = f"Write a bedtime story for {child_name} featuring {favorite_character} in {setting} with a {theme} theme."

    headers = {"Authorization": f"Bearer {DEEPSEEK_API_KEY}", "Content-Type": "application/json"}
    data = {"model": "deepseek-chat", "messages": [{"role": "user", "content": prompt}], "temperature": 0.7}

    response = requests.post(DEEPSEEK_API_URL, headers=headers, json=data)

    return response.json()["choices"][0]["message"]["content"] if response.status_code == 200 else "Error generating story."