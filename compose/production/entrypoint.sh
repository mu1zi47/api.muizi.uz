#!/bin/bash
set -e

echo "Applying migrations..."
python manage.py migrate

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Starting Gunicorn..."
gunicorn muiziBackend.wsgi:application --bind 0.0.0.0:8000 --workers 3 --timeout 120
