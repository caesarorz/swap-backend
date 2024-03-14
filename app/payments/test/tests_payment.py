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
# PAYMENTS_CREATE_URL = reverse('paymentmethod:create')

def payment_url(payment_id):
    """Create and return a payment detail URL."""
    return reverse('payments:paymentmethod-detail', args=[payment_id])

def create_payment_method(**params):
    """Create new payment method"""
    defaults = {
      'name': "Test Payment",
      'is_active': True,
      'description': "Test description",
      'created_at': datetime.datetime.now().date(),
      'updated_at': datetime.datetime.now().date(),
      'created_by': ''
    }

    defaults.update(params)
    payment = PaymentMethod.objects.create(**defaults)
    return payment

def create_user(**params):
    """Create and return a new user."""
    defaults = {
      'email':'user@example.com',
      'name': 'Test User',
      'password':'test123'
    }
    defaults.update(params)
    return get_user_model().objects.create_user(**defaults)


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
        self.user = create_user()
        self.client.force_authenticate(self.user)

    def test_create_payment_method_model(self):
        """Test create a payment method in the system successful"""
        payment_method = create_payment_method(created_by=self.user)
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

    def test_payment_list_limited_to_user(self):
        """Test list of payments is limited to authenticated user."""
        other_user = create_user(email='other@example.com', password='test123')
        create_payment_method(
            name='Payment 1',
            created_by=self.user
        )
        create_payment_method(
            name='Other Payment',
            created_by=other_user
        )

        res = self.client.get(PAYMENTS_URL)

        payments = PaymentMethod.objects.filter(user=self.user)
        serializer = PaymentMethodSerializer(payments, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_get_payment_detail(self):
        """Test get payment detail."""
        payment = create_payment_method(
            name='Payment 1',
            created_by=self.user
        )

        url = payment_url(payment.id)
        res = self.client.get(url)

        serializer = PaymentMethodSerializer(payment)
