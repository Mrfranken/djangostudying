from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^herolist/$', views.herolist),
    url(r'^herolist/(\d+)/$', views.herolist),
]

