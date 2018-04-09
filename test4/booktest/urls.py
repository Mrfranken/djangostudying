from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(\d+)/$', views.show, name='show'),
    url(r'^(?P<id1>\d+)/(?P<id2>\d+)/$', views.show_reverse, name='show_reverse')
]
