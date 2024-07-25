echo >&2 'Migrating to Database'
python manage.py migrate --noinput

echo >&2 'collecting static files'
python manage.py collectstatic --noinput

echo >&2 'starting server'
python manage.py runserver 0.0.0.0:8000
# /usr/local/bin/gunicorn config.wsgi:application -w 5 -b :$PORT --reload
