from django.conf.urls import patterns, url

from mails import views

urlpatterns = patterns('',
	url(r'^old$', views.old, name='old'),
	url(r'^new$', views.new, name='new'),
)

