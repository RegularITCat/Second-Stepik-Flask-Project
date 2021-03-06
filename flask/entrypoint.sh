#!/bin/bash
set -e

echo "Waiting for postgres..."
while ! nc -z db 5432; do
  sleep 0.1
done
echo "PostgreSQL started"

#flask db init
#flask db migrate
flask db upgrade
#uwsgi app.ini
gunicorn -c gunicorn.py.ini run:app