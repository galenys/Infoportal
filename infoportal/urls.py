from django.conf.urls import url, include

from . import views

from django.contrib.auth import views as auth_views

app_name = 'infoportal'
urlpatterns = [
    url(r'^newpost/$', views.newpost, name='newpost'),
    url(r'^$', views.index, name='index'),
]
