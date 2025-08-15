# ============================== Dockerfile ===================================
# FROM python:3.11-slim
# WORKDIR /app
# COPY pyproject.toml poetry.lock* requirements.txt* ./
# RUN pip install -r requirements.txt || true
# COPY . .
# ENV FLASK_APP=wsgi:app
# EXPOSE 5000
