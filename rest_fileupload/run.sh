#!/usr/bin/env bash

python manage.py makemigrations && \
python manage.py migrate && \
python manage.py adduser && \
python manage.py collectstatic --noinput && \
exec gunicorn rest_fileupload.wsgi:application --bind 0.0.0.0:8000 --workers 3