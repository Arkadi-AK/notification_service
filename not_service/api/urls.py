from rest_framework import routers

from api import views

router = routers.DefaultRouter()
router.register(r'client', views.ClientViewSet, basename='client')
router.register(r'sender', views.SenderViewSet, basename='sender')
urlpatterns = router.urls
