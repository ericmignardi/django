from django.urls import path
from .views import get_prices, chat_history

urlpatterns = [
    path('prices', get_prices, name='get-prices'),
    path('chat-history', chat_history, name='chat-history'),
]