from rest_framework import serializers
from .models import GrainPrice, ChatMessage

class GrainPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrainPrice
        fields = ['grain_type', 'price', 'date']

class ChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = ['role', 'content', 'created_at']