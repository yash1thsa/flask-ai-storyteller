# flask-ai-storyteller
Story teller app for Reya

# ============================== Quick notes ==================================
# 1) Start Redis, Flask, Celery worker. If using docker-compose, just `docker compose up`.
# 2) If running locally without Docker:
#    export FLASK_APP=wsgi:app
#    python manage.py   # creates DB
#    celery -A worker.celery worker --loglevel=INFO
#    flask run
# 3) POST /stories with JSON {child_name, favorite_character, setting, theme}
#    -> returns {story_id, task_id, status:"queued"}
#    GET /stories/<story_id> to fetch status & text.
# 4) If you see Connection refused to Ollama, ensure `ollama serve` is running
#    and OLLAMA_API_URL is reachable from the worker (host.docker.internal if Docker).


docker
------
docker build -t my-flask-app
docker run -p 8000:8000 my-flask-app

venv
----
python3 -m venv venv
source venv/bin/activate
pip3 install --upgrade pip setuptools wheel


local
-----
pip3 install --no-cache-dir -r requirements.txt 
brew install redis
brew services start redis
celery -A app.celery_app.celery worker --loglevel=info
python3 run.py  



which pip3
pip3 show celery



