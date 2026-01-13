from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import GrainPrice


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
        self.assertEqual(response.data[0]['grain_type'], 'Wheat')
        self.assertEqual(response.data[0]['price'], '7.50')


class ChatAPITests(APITestCase):
    """Tests for the chat API endpoints."""

    def test_chat_history_returns_200(self):
        """GET /api/chat-history should return 200 OK."""
        response = self.client.get('/api/chat-history')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)
