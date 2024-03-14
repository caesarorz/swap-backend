"""
Views for payment methods API
"""

from django.http import Http404
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.settings import api_settings
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import PaymentMethod
from .serializers import PaymentMethodSerializer, PaymentMethodDetailSerializer


class PaymentMethodsViewSet(ModelViewSet):
    """View for manage payment methods APIs
    """
    serializer_class = PaymentMethodDetailSerializer
    queryset = PaymentMethod.objects.all()
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        """Retrive payment methods for authenticated users"""
        return self.queryset.filter(created_by=self.request.user).order_by('-id')

    def get_serializer_class(self):
        """"""
        if self.action == 'list':
            return PaymentMethodSerializer
        return self.serializer_class

    def get(self, request, format=None):
        users = PaymentMethod.objects.all()
        serializer = PaymentMethodSerializer(users, many=True)
        return Response(serializer.data)
