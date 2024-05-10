from django.urls import path
from game.consumers import TicTacToeConsumer

websocket_urlpatterns = [
    path('ws/play/<room_name>/', TicTacToeConsumer.as_asgi()),
]