from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.resident_list, name='resident_list'),
]