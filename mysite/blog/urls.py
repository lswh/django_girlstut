from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
    url(r'', views.post_list),
)
