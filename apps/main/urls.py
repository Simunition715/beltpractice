from django.conf.urls import url
from . import views
# from django.contrib import admin

urlpatterns = [
    url(r'^$',views.index),
    url(r'^register$',views.register),
    url(r'^dashboard$',views.dashboard),
    url(r'^logout$',views.logout),
    url(r'^login$',views.login),
    url(r'^add$',views.add),
    url(r'^postit$',views.postit),
    url(r'^plus$',views.plus),
    url(r'^remove/(?P<id>\d+)$',views.remove),
    url(r'^show/(?P<id>\d+)$', views.show),





]