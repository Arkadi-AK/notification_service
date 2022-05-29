from datetime import datetime

from api.post_sender import send_message
from not_service.celery import app


# @app.task
# def send_message_task(queryset, text):
#     print("Сработала ** send_message_task")
#     send_message(queryset, text)
#
#
# @app.task
# def send_message_task2(queryset, text, start_mailing, stop_mailing):
#     print("Сработала send_message_task_2")
#     now = datetime.utcnow().strftime('%Y.%m.%d %H:%M:%S')
#     if start_mailing < now < stop_mailing:
#         send_message(queryset, text)
#
#
# @app.task
# def print_word(arg1=1, arg2=2):
#     print("FOO")


@app.task
def send_message_task(**kwargs):
    queryset = kwargs['queryset']
    text = kwargs['text']
    send_message(queryset, text)


# @app.task
# def send_message_task2(queryset, text, start_mailing, stop_mailing, sender_id):
#     print("Сработала send_message_task_2")
#     now = datetime.utcnow().strftime('%Y.%m.%d %H:%M:%S')
#
#     if start_mailing < now < stop_mailing:
#         send_message(queryset, text)
#         print("распечатка функц")
#     else:
#         print("PERIOD *** TASK")
#         PeriodicTask.objects.create(
#             name=sender_id,
#             task='repeat_order_make',
#             interval=IntervalSchedule.objects.get(every=10, period='seconds'),
#             args=json.dumps([queryset, sender_id]),
#             start_time=timezone.now(),
#         )
#
#
# @shared_task(name="repeat_order_make")
# def repeat_order_make(*args):
#     s = send_message(args[0], args[-1])
#     print(s, '**')
#     # order = Order.objects.get(pk=order_id)
#     order = 1
#     # if order.status != '0':
#     if order != '0': # убрать это условие
#         print('Статус получен!')
#         task = PeriodicTask.objects.get(name=args[-1])
#         task.enabled = False
#         task.save()
#     else:
#         # Необходимая логика при повторной отправке заказа
#         print('Я должна повторно оформлять заказ каждые 10 секунд')