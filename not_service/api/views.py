from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from api.serializers import (ClientListSerializer, SenderListSerializer)
from notify_sender.models import Client, Sender


class ClientViewSet(ModelViewSet):
    model = Client
    queryset = model.objects.all()
    serializer_class = ClientListSerializer
    permission_classes = (IsAdminUser,)


class SenderViewSet(ModelViewSet):
    model = Sender
    queryset = model.objects.all()
    serializer_class = SenderListSerializer
    permission_classes = (IsAdminUser,)
