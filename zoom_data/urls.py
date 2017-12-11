from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name = 'home'),
    url(r'^residents/$', views.resident_list, name='resident_list'),
    url(r'^resident/(?P<pk>\d+)/$', views.resident_detail, name='resident_detail'),
    url(r'^goal/new/$', views.goal_new, name='goal_new'),
    url(r'^resident/new/$', views.resident_new, name = 'resident_new'),
]