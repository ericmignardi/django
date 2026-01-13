from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import GrainPrice, ChatMessage


class GrainPriceAPITests(APITestCase):
    """Tests for the grain price API endpoints."""

    def setUp(self):
        """Create test data before each test."""
        GrainPrice.objects.create(grain_type='Wheat', price=7.50)
        GrainPrice.objects.create(grain_type='Corn', price=5.25)
        GrainPrice.objects.create(grain_type='Canola', price=12.00)

    def test_get_prices_returns_200(self):
        """GET /api/prices should return 200 OK with price data."""
        response = self.client.get('/api/prices')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_get_prices_returns_correct_fields(self):
        """Response should contain grain_type and price fields."""
        response = self.client.get('/api/prices')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.data[0]['grain_type'], 'Wheat')
        self.assertEqual(response.data[0]['price'], 7.50)

    def test_get_prices_empty_database(self):
        """Should return empty list when no prices exist."""
        GrainPrice.objects.all().delete()
        response = self.client.get('/api/prices')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)
        pass


class ChatMessageModelTests(TestCase):
    """Tests for the ChatMessage model."""

    def test_chat_message_creation(self):
        """ChatMessage should be created with correct fields."""
        message = ChatMessage.objects.create(
            grain_type='Wheat',
            price=7.50,
            created_at='2022-01-01T00:00:00Z',
        )
        self.assertEqual(message.grain_type, 'Wheat')
        self.assertEqual(message.price, 7.50)
        self.assertEqual(message.created_at, '2022-01-01T00:00:00Z')

    def test_chat_messages_ordered_by_created_at(self):
        """Messages should be ordered by creation time."""
        message1 = ChatMessage.objects.create(
            grain_type='Wheat',
            price=7.50,
            created_at='2022-01-01T00:00:00Z',
        )
        message2 = ChatMessage.objects.create(
            grain_type='Corn',
            price=5.25,
            created_at='2022-01-02T00:00:00Z',
        )
        messages = ChatMessage.objects.all()
        self.assertEqual(messages[0], message2)
        self.assertEqual(messages[1], message1)


class ChatAPITests(APITestCase):
    """Tests for the chat API endpoints."""

    def test_chat_history_returns_200(self):
        """GET /api/chat-history should return 200 OK."""
        response = self.client.get('/api/chat-history')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_chat_post_without_message_returns_error(self):
        """POST /api/chat without message should return error."""
        response = self.client.post('/api/chat')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
