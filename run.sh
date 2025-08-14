#!/bin/bash

# Stop on error
set -e

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Start Redis server in the background
echo "Starting Redis..."
redis-server --daemonize yes

# Export Flask environment variables
export FLASK_APP=run.py
export FLASK_ENV=production

# Start Celery worker in the background
echo "Starting Celery worker..."
celery -A app.celery_app.celery worker --loglevel=info &

# Start Flask app
echo "Starting Flask app..."
flask run