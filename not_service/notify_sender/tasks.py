from api.post_sender import send_message
from not_service.celery import app


@app.task
def send_message_task(**kwargs):
    queryset = kwargs['queryset']
    text = kwargs['text']
    send_message(queryset, text)
