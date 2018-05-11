from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(\d+)/$', views.show, name='show'),
    # 改变这个路径后如果之前从不同的地方访问这个链接，一个是正常的解析，一个是反向及解析，当改变
    # 这个url之后反向解析不会受到影响
    url(r'^(?P<id1>\d+)/(?P<id2>\d+)/$', views.show_reverse, name='show_reverse'),
    url(r'^index2/$', views.index2, name='index2'),
    url(r'^user1/$', views.user1, name='user1'),
    url(r'^user2/$', views.user2, name='user2'),
    url(r'^htmltest/$', views.htmlzhuanyitest, name='htmltest'),
    url(r'^csrf1/$', views.csrf1, name='csrf1'),
    url(r'^csrf2/$', views.csrf2, name='csrf2'),
    url(r'^verify_code/$', views.verify_code_test, name="verify_code"),
    url(r'^verifytest1/$', views.verifytest1, name="verifytest1"),
    url(r'^verifytest2/$', views.verifytest2, name="verifytest2"),
]
