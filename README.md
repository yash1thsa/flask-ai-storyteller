# flask-ai-storyteller
Story teller app for Reya


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
brew services start redis
celery -A celery_app.celery worker --loglevel=info
python3 run.py  



which pip3
pip3 show celery



