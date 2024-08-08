#!/bin/bash

# Function to check if the database is up
check_db() {
  nc -z db 5432
}

# Wait for the database to be ready
until check_db; do
  echo "Waiting for database..."
  sleep 1
done

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Run the application
gunicorn things.wsgi:application --bind 0.0.0.0:8000
