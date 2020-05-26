#!/bin/bash
set -e

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

flask db upgrade
#uwsgi app.ini
gunicorn -c gunicorn.py.ini run:app