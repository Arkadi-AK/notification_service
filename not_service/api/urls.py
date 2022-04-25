from rest_framework import routers

from api import views

router = routers.DefaultRouter()
router.register(r'client', views.ClientViewSet, basename='client')
router.register(r'sender', views.SenderViewSet, basename='sender')
# router.register(r'clients/(?P<id>\d+)', views.ClientViewSet)
# router.register(r'tickets/(?P<id>\d+)/messages', views.MessagesViewSet)
urlpatterns = router.urls
