from django.conf.urls import url
from . import views

urlpatterns = [
    
    url(r'^$', views.posts_home),
    url(r'^create/$', views.posts_create),
    url(r'^detail/(?P<id>\d+)/$', views.posts_detail),
    url(r'^list/$', views.posts_list),
    url(r'^update/$', views.posts_update),
    url(r'^delete/$', views.posts_delete),
    url(r'^return/$', views.posts_return),
]
