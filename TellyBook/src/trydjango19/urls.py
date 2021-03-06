"""trydjango19 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from posts import views
from check.views import check_add,check_return,check_verify,profcontact,dev_detail, imagetest,test_fcm
from book_detail.views import track_return, events, on_action, input_detail
from check_room.views import roomsugg, dash_history,noti

urlpatterns = [
    url(r'^$', views.start),
    url(r'^admin/', admin.site.urls),
    url(r'^posts/', include("posts.urls")),
    url(r'^test/add/', check_add),
    url(r'^test/return/',check_return),
    url(r'^test/',check_verify),
    url(r'^bookdetail/input',input_detail),
    url(r'^track/',track_return),
    url(r'^events/',events),
    url(r'^onaction/',on_action),
    url(r'^dev/',dev_detail),
    url(r'^prof/',profcontact),
    url(r'^history/',dash_history),
    url(r'^roomsugg/',roomsugg),
    url(r'^abc/',imagetest),
    url(r'^noti/',noti),
    url(r'^test_fcm/',test_fcm),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
