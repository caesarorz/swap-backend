"""
Views for user API
"""

from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from users.serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    """Create a new user type staff."""
    serializer_class = UserSerializer
