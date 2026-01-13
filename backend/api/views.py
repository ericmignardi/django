from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import GrainPrice, ChatMessage
from .serializers import GrainPriceSerializer, ChatMessageSerializer

@api_view(['GET'])
def get_prices(request):
    prices = GrainPrice.objects.all()
    serializer = GrainPriceSerializer(prices, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def chat_history(request):
    messages = ChatMessage.objects.all()
    serializer = ChatMessageSerializer(messages, many=True)
    return Response(serializer.data)