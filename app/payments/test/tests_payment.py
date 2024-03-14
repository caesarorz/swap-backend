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

LIST_PAYMENTS_URL = reverse('payments:list')
CREATE_PAYMENT_USER_URL = reverse('payments:create')


def create_payment_method(**params):
    defaults = {
      'name': "Test Payment",
      'is_active': True,
      'description': "Test description",
      'created_at': datetime.datetime.now().date(),
      'updated_at': datetime.datetime.now().date()
    }

    defaults.update(params)
    return defaults


class PaymentMethodsTestUnauthenticated(TestCase):
    """Test payment methods"""

    def setUp(self):
        """Set client for testing"""
        self.client = APIClient()

    def test_payments_auth_required(self):
        """Test auth is required to call API"""
        res = self.client.get(LIST_PAYMENTS_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PaymentMethodsTestAuthenticated(TestCase):
    """Test payment methods with authenticated user"""

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            'user@test.com',
            'testpass123',
        )
        self.client.force_authenticate(self.user)

    def test_retrieve_payments(self):
        """Test payment methods list endpoint user authenticated"""
        create_payment_method(name='Payment 1')
        create_payment_method(name='Payment 2')
        res = self.client.get(LIST_PAYMENTS_URL)

        payments = PaymentMethod.objects.all()
        serializer = PaymentMethodSerializer(payments, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_create_payment_method_model(self):
        """Test create a payment method in the system successful"""
        created_payment_method = create_payment_method(name='Payment 1')
        payment_method = PaymentMethod.objects.create(**created_payment_method)

        self.assertEqual(str(payment_method), payment_method.name)

    # def test_create_payment_method_endpoint(self):
    #     """Test create payment method from endpoint"""
    #     created_payment_method = create_payment_method(name='Payment 1')
    #     res = self.client.get(CREATE_PAYMENT_USER_URL)

    #     serializer = PaymentMethodSerializer(created_payment_method)
    #     self.assertEqual(res.status_code, status.HTTP_200_OK)


