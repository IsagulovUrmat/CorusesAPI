web: gunicorn —chdir courses courses.wsgi:application
python manage.py collectstatic --noinput
manage.py migrate