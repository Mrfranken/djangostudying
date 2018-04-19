from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^booktest/$', views.execptiontest_func),
    url(r'^uploadpic/$', views.upload_pic),
    url(r'^uploadhandle/$', views.uploadhandle)
]