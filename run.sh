#!/bin/bash

echo '=== Preparing DB ==='
python manage.py makemigrations
python manage.py migrate --noinput

echo '=== Preparing Static files ==='
python manage.py collectstatic --noinput

echo '=== Run APP ==='
exec gunicorn --bind=0.0.0.0:8001 --workers=5 staff.wsgi