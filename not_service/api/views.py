from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from api.serializers import (ClientSerializer)
from notify_sender.models import Client


class ClientViewSet(ModelViewSet):
    model = Client
    queryset = model.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (IsAdminUser,)
