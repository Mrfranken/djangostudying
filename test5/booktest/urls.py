from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^booktest/$', views.execptiontest_func),
    url(r'^uploadpic/$', views.upload_pic),
    url(r'^uploadhandle/$', views.uploadhandle),
    url(r'^booktest/editor/$', views.editor),
    url(r'^booktest/content/$', views.show_editor_content),
    url(r'^cache/$', views.cache_view_test),
    url(r'^cache_template/$', views.cache_template_test),
    url(r'^cache_data/$', views.cache_data),
]
