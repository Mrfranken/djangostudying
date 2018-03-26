from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^book/([0-9]+)/', views.detail),
    url(r'^(\d+)/', views.show, name='show')
]
