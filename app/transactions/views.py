"""Views for transactions methods API"""

from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.settings import api_settings
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Transaction
from .serializers import TransactionSerializer


class TransactionViewSet(ModelViewSet):
    """View to manage transactions in general"""
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()
    authentication_classes = [JWTAuthentication]
