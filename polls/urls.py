#Author: Vinay vittal karagod
# Holds the various URL links of the application

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^(?P<Dtc_code>[0-9]+)/$', views.create, name='create'),
	url(r'^(?P<Dtc_code>[0-9]+)/detail/$', views.detail, name='detail'),
    url(r'^(?P<Dtc_code>[0-9]+)/update/$', views.update, name='update'),
	url(r'^(?P<Dtc_code>[0-9]+)/delete/$', views.delete, name='delete'),
]