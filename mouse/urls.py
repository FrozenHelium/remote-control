from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^offset/(?P<xpos>[+-]?[0-9]+)/(?P<ypos>[+-]?[0-9]+)/$', views.offset, name='offset'),
    url(r'^left_click$', views.left_click, name='left_click'),
    url(r'^right_click$', views.right_click, name='right_click'),
]
