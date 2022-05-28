import time

from django.core.mail import send_mail


def send(user_email):
    time.sleep(5)
    print("Печатаем емеил++", user_email)
    # send_mail(
    #     'Вы подписались на рассылку',
    #     'Мы будем присылать вам много спама',
    #     'django@mail.com',
    #     [user_email],
    #     fail_silently=False,
    # )


def my_print():
    print("Печатаю мой принт")
