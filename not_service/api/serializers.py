from rest_framework.fields import SerializerMethodField
from rest_framework.relations import HyperlinkedIdentityField
from rest_framework.serializers import (ModelSerializer)

from notify_sender.models import Client, Sender


class ClientListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(view_name='client-detail')

    class Meta:
        model = Client
        queryset = model.objects.all()
        fields = ('url', 'phone_number', 'code_operator', 'teg', 'time_zone')


class ClientDetailSerializer(ModelSerializer):
    client = SerializerMethodField(read_only=True)

    def get_client(self, obj):
        return str(obj.client.phone_number)

    class Meta:
        model = Client
        fields = ('url', 'phone_number', 'code_operator', 'teg', 'time_zone')


class SenderListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(view_name='sender-detail')

    class Meta:
        model = Sender
        queryset = model.objects.all()
        fields = ('url', 'start_mailing', 'stop_mailing', 'text', 'filter')
