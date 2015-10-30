from django.conf.urls import url, include
from rest_framework import routers
import views

router = routers.DefaultRouter()
router.register(r'ddjjs', views.DDJJBienViewSet, 'api-ddjjs-bienes')
router.register(r'legisladores', views.PersonaViewSet, 'api-legisladores')

urlpatterns = [
    url(r'^', include(router.urls)),
]
