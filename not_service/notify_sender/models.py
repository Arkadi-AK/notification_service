from datetime import datetime
from django.utils import timezone
from django.utils.timezone import activate

from django.utils.timezone import localtime, now

# get now datetime based upon django settings.py TZ_INFO
from notify_sender.tasks import send_message_task, send_message_task2

l = localtime(now())




from not_service import settings

# activate(settings.TIME_ZONE)


from django.db import models

from api.post_sender import send_message


class Client(models.Model):
    phone_number = models.CharField(max_length=10, null=False, verbose_name='Номер телефона')
    code_operator = models.SmallIntegerField(null=False, verbose_name='Код моб. оператора')
    teg = models.CharField(max_length=100, null=True, verbose_name='Тег')
    time_zone = models.CharField(max_length=7, null=True, verbose_name='Часовой пояс')

    def __str__(self):
        return f"Клиент {self.phone_number}"

    class Meta:
        ordering = ['id']
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Sender(models.Model):
    start_mailing = models.DateTimeField(null=False, verbose_name='Время запуска рассылки')
    stop_mailing = models.DateTimeField(null=False, verbose_name='Время окончания рассылки')
    text = models.TextField(blank=True)
    filter = models.CharField(max_length=255, null=True, verbose_name='Фильтр')

    def __str__(self):
        return f"Рассылка {self.id}"

    def select_clients_with_filter(self):
        print("Сработал метод select_clients_with_filter")
        text = self.text
        filter = self.filter
        start_mailing = self.start_mailing.strftime('%Y.%m.%d %H:%M:%S')
        stop_mailing = self.stop_mailing.strftime('%Y.%m.%d %H:%M:%S')
        now = datetime.utcnow().strftime('%Y.%m.%d %H:%M:%S')
        if filter:
            queryset = Client.objects.filter(teg=filter).values('id', 'phone_number')
        else:
            queryset = Client.objects.all().values('id', 'phone_number')
        queryset = list(queryset)
        send_message_task2.delay(queryset, text, start_mailing, stop_mailing)

        # if start_mailing < now < stop_mailing:
        #     print("дата в пределах")
        #     queryset = Client.objects.filter(teg=filter).values('id', 'phone_number')
        #     queryset = list(queryset)
            # Отправка сообщения на url адрес
            # send_message_task.delay(queryset, text)
            # send_message_task2.delay(text)
            # return queryset

    def save(self, *args, **kwargs):
        self.select_clients_with_filter()
        print("Сработал метод save в модели")
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['id']
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


class Message(models.Model):
    created_at = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
    status = models.CharField(max_length=50, null=True, verbose_name='Статус отправки')
    mailing = models.ForeignKey(Sender, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return f"Сообщение {self.id}"

    class Meta:
        ordering = ['id']
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
