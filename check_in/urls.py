from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^groups$', views.user_groups, name='user_groups'),
]
