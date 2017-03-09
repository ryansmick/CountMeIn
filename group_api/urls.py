from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.GroupAPI.as_view(), name='group_rest'),
]
