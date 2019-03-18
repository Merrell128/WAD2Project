from django.conf.urls import url
from restaurants import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^add_restaurant/$', views.add_restaurant, name='add_restaurant'),
    url(r'^add_review/$', views.add_review, name='add_review'),    
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$',
        views.show_restaurant, name='show_category'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^restricted/', views.restricted, name='restricted'),
    url(r'^logout/$', views.user_logout, name='logout'),


]
