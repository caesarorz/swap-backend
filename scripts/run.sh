#!/bin/sh

set -e

python manage.py wait_db_is_up
python manage.py collectstatic --noinput
python manage.py migrate

uwsgi --socket :9000 --workers 4 --master --enable-threads --module app.wsgi
