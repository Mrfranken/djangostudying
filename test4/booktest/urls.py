from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # 原本是r'^(\d+)/$'这个但是如果变成r'^3(\d+)/$'只有index.html中的<a href="1">就失效了
    url(r'^3(\d+)/$', views.show, name='show'),
    # 反向解析的意思就是说无论这个位置以后改成什么样子都能通过不修改模板中url来保证这个url的有效性
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
