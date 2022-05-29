import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'not_service.settings')

app = Celery('send_message')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
