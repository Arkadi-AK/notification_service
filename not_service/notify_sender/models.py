from django.db import models

from notify_sender.tasks import send_message_task


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

    def save(self, *args, **kwargs):
        text = self.text
        filter = self.filter
        eta = self.start_mailing
        expires = self.stop_mailing
        if filter:
            queryset = Client.objects.filter(teg=filter).values('id', 'phone_number')
        else:
            queryset = Client.objects.all().values('id', 'phone_number')
        queryset = list(queryset)
        super().save(*args, **kwargs)
        kw = {'queryset': queryset, 'text': text}
        send_message_task.apply_async(eta=eta, expires=expires, kwargs=kw)

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
