import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'not_service.settings')

app = Celery('send_message')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# app.conf.beat_schedule = {
#     'send-spam-every-1-minute': {
#         'task': 'main.tasks.print_word',
#         'schedule': crontab(minute='*/1'),
#     },
# }



app.conf.beat_schedule = {
    # Executes every Monday morning at 7:30 a.m.
    'add-every-monday-morning': {
        'task': 'notify_sender.tasks.print_word',
        'schedule': crontab(hour=14, minute=00),
        'args': (16, 16),
    },
}
