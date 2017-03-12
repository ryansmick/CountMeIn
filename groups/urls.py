from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.groups, name='groups'),
	url(r'^api$', views.GroupAPI.as_view(), name='group_api'),
]
