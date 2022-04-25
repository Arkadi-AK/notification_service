from rest_framework import routers

from api import views

router = routers.DefaultRouter()
router.register(r'clients', views.ClientViewSet, basename='clients')
# router.register(r'tickets', views.TicketViewSet, basename='tickets')
# router.register(r'tickets/(?P<id>\d+)/messages', views.MessagesViewSet)
urlpatterns = router.urls
