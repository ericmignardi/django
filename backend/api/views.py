from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import GrainPrice, ChatMessage
from .serializers import GrainPriceSerializer, ChatMessageSerializer
from .ai import client
from pydantic import BaseModel, Field


class GeminiResponse(BaseModel):
    text: str = Field(description="Gemini API response text field")

# Create your views here.

@api_view(['GET'])
def get_prices(request):
    prices = GrainPrice.objects.all()
    serializer = GrainPriceSerializer(prices, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def chat(request):
    try:
        message = request.data.get('message')
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=message,
            config={
                "response_mime_type": "application/json",
                "response_json_schema": GeminiResponse.model_json_schema(),
            }
        )
        responseJson = GeminiResponse.model_validate_json(response.text)
        ChatMessage.objects.create(role='assistant', content=responseJson.text)
        return Response(responseJson.model_dump())  # Return serialized model
    except ValueError as e:
        return Response({'error': f'Invalid response format: {str(e)}'}, status=400)
    except Exception as e:
        if '503' in str(e):
            return Response({'error': 'Service unavailable. Please try again later.'}, status=503)
        return Response({'error': str(e)}, status=400)

@api_view(['GET'])
def chat_history(request):
    messages = ChatMessage.objects.all()
    serializer = ChatMessageSerializer(messages, many=True)
    return Response(serializer.data)