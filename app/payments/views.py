"""
Views for payment methods API
"""

from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status, generics, authentication, permissions
from rest_framework.settings import api_settings
from rest_framework.response import Response

from .models import PaymentMethod
from .serializers import PaymentMethodSerializer


class PaymentMethodList(APIView):
    """
    List all payments
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        users = PaymentMethod.objects.all()
        serializer = PaymentMethodSerializer(users, many=True)
        return Response(serializer.data)