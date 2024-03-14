"""
Tests for the payments API.
"""
import datetime
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from payments.models import PaymentMethod
from payments.serializers import PaymentMethodSerializer

PAYMENTS_URL = reverse('payments:paymentmethod-list')


def create_payment_method(**params):
    defaults = {
      'name': "Test Payment",
      'is_active': True,
      'description': "Test description",
      'created_at': datetime.datetime.now().date(),
      'updated_at': datetime.datetime.now().date(),
      'created_by': ''
    }

    defaults.update(params)
    return defaults


class PaymentMethodsTestUnauthenticated(TestCase):
    """Test payment methods"""

    def setUp(self):
        """Set client for testing"""
        self.client = APIClient()

    # def test_auth_required(self):
    #     """Test auth is required to call API."""
    #     res = self.client.get(PAYMENTS_URL)

    #     self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PaymentMethodsTestAuthenticated(TestCase):
    """Test payment methods with authenticated user"""

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            'user@test.com',
            'testpass123',
        )
        self.client.force_authenticate(self.user)

    def test_create_payment_method_model(self):
        """Test create a payment method in the system successful"""
        created_payment_method = create_payment_method(
            name='Payment 1',
            created_by=self.user
        )
        payment_method = PaymentMethod.objects.create(**created_payment_method)

        self.assertEqual(str(payment_method), payment_method.name)

    def test_retrieve_payment_methods(self):
        """Test retrieving a list of payment methods."""
        create_payment_method(
            name='Payment 1',
            created_by=self.user
        )
        create_payment_method(
            name='Payment 2',
            created_by=self.user
        )

        res = self.client.get(PAYMENTS_URL)

        payment_methods = PaymentMethod.objects.all().order_by('-id')
        serializer = PaymentMethodSerializer(payment_methods, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)


