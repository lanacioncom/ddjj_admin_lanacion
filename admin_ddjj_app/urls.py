from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    url(r'^tipo_bien/', views.tipo_bien, name='tipo_bien'),
)
