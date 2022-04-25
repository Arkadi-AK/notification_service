from django.contrib.auth import get_user_model
from rest_framework.serializers import (ModelSerializer)

from notify_sender.models import Client


class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        queryset = model.objects.all()
        fields = ('phone_number', 'code_operator', 'teg', 'time_zone')
        # extra_kwargs = {'password': {'write_only': True}}

    # def create(self, validated_data):
    #     phone_number = validated_data.pop('phone_number', 'code_operator')
    #     client = self.Meta.model(**validated_data)
    #     client.set_password(phone_number)
    #     client.save()
    #     return client
    #
    # def update(self, instance, validated_data):
    #     instance.set_password(validated_data.pop('password', ''))
    #     return super().update(instance, validated_data)
