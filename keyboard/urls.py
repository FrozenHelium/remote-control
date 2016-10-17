from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^tap_character/(?P<character>.)/$',  views.tap_character,  name='tap_character'),

    url(r'^tap_left_key$',  views.tap_left_key,  name='tap_left_key'),
    url(r'^tap_right_key$', views.tap_right_key, name='tap_right_key'),
    url(r'^tap_up_key$',    views.tap_up_key,    name='tap_up_key'),
    url(r'^tap_down_key$',  views.tap_down_key,  name='tap_down_key'),
    url(r'^tap_space_key$', views.tap_space_key, name='tap_space_key'),
    url(r'^tap_return_key$', views.tap_return_key, name='tap_return_key'),
    url(r'^tap_backspace_key$',  views.tap_backspace_key,  name='tap_backspace_key'),

    url(r'^press_ctrl_key$',    views.press_ctrl_key,   name='press_ctrl_key'),
    url(r'^release_ctrl_key$',  views.release_ctrl_key, name='release_ctrl_key'),

    url(r'^press_shift_key$',   views.press_shift_key,   name='press_shift_key'),
    url(r'^release_shift_key$', views.release_shift_key, name='release_shift_key'),

    url(r'^press_alt_key$',     views.press_alt_key,    name='press_alt_key'),
    url(r'^release_alt_key$',   views.release_alt_key,  name='release_alt_key'),

    url(r'^press_win_key$',     views.press_win_key,    name='press_win_key'),
    url(r'^release_win_key$',   views.release_win_key,  name='release_win_key'),
]
