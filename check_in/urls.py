from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^groups$', views.user_groups, name='user_groups'),
	url(r'^api/groups$', views.GroupREST.as_view(), name='group_rest'),
]
