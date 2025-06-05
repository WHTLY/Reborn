#!/bin/sh
# Apply database migrations and execute the command
python manage.py migrate --noinput
exec "$@"
