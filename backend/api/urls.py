from django.urls import path
from .views import get_prices, chat, chat_history

urlpatterns = [
    path('prices', get_prices, name='get-prices'),
    path('chat', chat, name='chat'),
    path('chat-history', chat_history, name='chat-history'),
]