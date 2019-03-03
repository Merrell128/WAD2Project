from django.conf.urls import url
from restaurants import views

urlpatterns = [
	url(r'^$', views.index, name='index'),

	url(r'^about/',views.about, name = 'about'),

	url(r'^register/$',
        views.register, name='register'),

	url(r'^login/$', views.user_login, name='login'),


]
