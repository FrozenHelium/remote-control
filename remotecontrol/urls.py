from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^main/', include('main.urls')),
    url(r'^volume/', include('volume.urls')),
    url(r'^keyboard/', include('keyboard.urls')),
    url(r'^mouse/', include('mouse.urls')),
    url(r'^admin/', admin.site.urls),
]
