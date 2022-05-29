from django.db.models.signals import post_save
from django.dispatch import receiver

from notify_sender.models import Sender, Message, Client


@receiver(post_save, sender=Sender)
def post_save_sender(created, **kwargs):
    instance = kwargs['instance']
    clients = Client.objects.filter(teg=instance.filter).all()
    if created:
        for client in clients:
            Message(status="Отправлено", mailing=instance, client=client).save()
            print(f'Сообщение с текстом {instance.text} для клиента {client.phone_number} создано')
    else:
        print(f'Рассылка {instance} обновлена')
