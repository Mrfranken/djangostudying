from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(\d+)/$', views.detail, name='detail'),
    # 这种形式的参数只能通过获取url中的参数来获得
    url(r'^(?P<id1>\d+)/(?P<id2>\d+)/$', views.ganjianzhiparams, name='params'),
    # 这种形式的参数只能通过request方式获得
    url(r'^getTest1/$', views.getTest1),
    url(r'^getTest2/$', views.getTest2),
    url(r'^getTest3/$', views.getTest3),
    url(r'^posttest1/$', views.posttest1),
    url(r'^posttest2/$', views.posttest2),
    url(r'^cookietest/$', views.cookietest),
    url(r'^redirect1/$', views.redtest1),
    url(r'^redirect2/$', views.redtest2),
    url(r'^session1/$', views.session1),
    url(r'^session2/$', views.session2),
    url(r'^session2_handle/$', views.session2_handle),
    url(r'^session3/$', views.session3)
]

# URL的反向解析
# 如果在视图、模板中使用硬编码的链接，在urlconf发生改变时，维护是一件非常麻烦的事情
# 解决：在做链接时，通过指向urlconf的名称，动态生成链接地址
# 视图：使用django.core.urlresolvers.reverse()函数
# 模板：使用url模板标签
