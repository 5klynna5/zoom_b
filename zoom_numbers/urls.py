from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^ymca_visits/$', views.ymca_visits, name = 'ymca_visits'),
]