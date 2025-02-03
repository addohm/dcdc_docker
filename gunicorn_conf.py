# /home/addohm/cdc_django/cdc_project/gunicorn_conf.py
# screen gunicorn -c gunicorn_conf.py cdc_project.wsgi:application
bind = '0.0.0.0:8000'
worker_class = 'sync'
loglevel = 'debug'
accesslog = '/var/log/gunicorn/cdc-django_access_log'
acceslogformat ="%(h)s %(l)s %(u)s %(t)s %(r)s %(s)s %(b)s %(f)s %(a)s"
errorlog =  '/var/log/gunicorn/cdc-django_error_log'
