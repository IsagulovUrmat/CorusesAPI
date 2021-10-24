web: gunicorn --chdir courses courses.wsgi
python manage.py collectstatic --noinput
manage.py migrate