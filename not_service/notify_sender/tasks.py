from datetime import datetime

from api.post_sender import send_message
from not_service.celery import app


@app.task
def send_message_task(queryset, text):
    print("Сработала ** send_message_task")
    send_message(queryset, text)


@app.task
def send_message_task2(queryset, text, start_mailing, stop_mailing):
    print("Сработала send_message_task_2")
    now = datetime.utcnow().strftime('%Y.%m.%d %H:%M:%S')
    if start_mailing < now < stop_mailing:
        send_message(queryset, text)


@app.task
def print_word(arg1=1, arg2=2):
    print("FOO")
