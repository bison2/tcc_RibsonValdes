
web: gunicorn DBR_project.wsgi --preload --log-file -
python manage.py collectstatic --noinput 
release: python3 manage.py migrate