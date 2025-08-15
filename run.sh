#!/bin/bash
set -e

# ========= CONFIG =========
VENV_DIR=".venv"
PYTHON="python3"
DB_FILE="instance/app.db"
OLLAMA_URL="http://127.0.0.1:11434/api/generate"
CELERY_APP="worker.celery"
# ==========================

# Auto-detect FLASK_APP
if [ -f "wsgi.py" ]; then
    FLASK_APP="wsgi:app"
elif [ -f "app/wsgi.py" ]; then
    FLASK_APP="app.wsgi:app"
else
    echo "Cannot find wsgi.py. Exiting."
    exit 1
fi

export FLASK_APP=$FLASK_APP
export FLASK_ENV=development
export OLLAMA_API_URL=$OLLAMA_URL

echo "=== Activating virtual environment ==="
if [ ! -d "$VENV_DIR" ]; then
    echo "No venv found, creating one..."
    $PYTHON -m venv $VENV_DIR
fi
source $VENV_DIR/bin/activate

echo "=== Installing requirements ==="
pip install --upgrade pip
pip install -r requirements.txt

echo "=== Starting Ollama if not already running ==="
if ! pgrep -x "ollama" > /dev/null; then
    echo "Ollama not running — starting in background..."
    ollama serve > ollama.log 2>&1 &
    sleep 5
else
    echo "Ollama already running."
fi

echo "=== Initializing database ==="
if [ ! -f "$DB_FILE" ]; then
    echo "Creating DB..."
    flask db init || true
    flask db migrate -m "Initial migration"
    flask db upgrade
else
    echo "DB already exists."
fi

echo "=== Starting Celery worker ==="
pkill -f "celery" || true
celery -A $CELERY_APP worker --loglevel=INFO &
CELERY_PID=$!
sleep 2

echo "=== Starting Flask server ==="
flask run --host=0.0.0.0 --port=5001 &
FLASK_PID=$!
sleep 2

# Open browser to index page
if command -v xdg-open &>/dev/null; then
    xdg-open http://127.0.0.1:5001
elif command -v open &>/dev/null; then
    open http://127.0.0.1:5001
fi

echo "=== All services started ==="
echo "Flask PID: $FLASK_PID"
echo "Celery PID: $CELERY_PID"
echo "Visit: http://127.0.0.1:5001"

# Keep script running until killed
trap "kill $FLASK_PID $CELERY_PID" SIGINT
wait
