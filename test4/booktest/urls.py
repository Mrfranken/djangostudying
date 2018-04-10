from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(\d+)/$', views.show, name='show'),
    url(r'^(?P<id1>\d+)/(?P<id2>\d+)/$', views.show_reverse, name='show_reverse'),
    url(r'^index2/$', views.index2, name='index2'),
    url(r'^user1/$', views.user1, name='user1'),
    url(r'^user2/$', views.user2, name='user2'),
    url(r'^htmltest/$', views.htmlzhuanyitest, name='htmltest'),
    url(r'^csrf1/$', views.csrf1, name='csrf1'),
    url(r'^csrf2/$', views.csrf2, name='csrf2')
]
