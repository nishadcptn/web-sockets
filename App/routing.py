# chat/routing.py
from django.urls import path

from .consumers import *

websocket_urlpatterns = [
    path('ws/chat', ChatConsumer.as_asgi()),
    # re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
]