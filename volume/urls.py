from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^vol_increase$', views.vol_increase, name='vol_increase'),
    url(r'^vol_decrease$', views.vol_decrease, name='vol_decrease'),
]
