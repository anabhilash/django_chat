from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$',  views.landing, name='landingpage'),

    url(r'^new/$', views.new_room, name='new_room'),
    url(r'^room/(?P<label>[a-zA-Z]+)/$', views.chatroom, name='chat_room'),

    url(r'^register/$', views.clientregister, name='clientRegister'),
    url(r'^login/$', views.clientlogin, name='clientLogin')
]
