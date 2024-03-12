"""
Views for user API
"""
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
# custom token
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from .models import User
from users.serializers import UserSerializer, AuthTokenSerializer, ClientSerializer


class AuthTokenView(ObtainAuthToken):
    """Create a new auth token for user."""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })


class CreateUserView(generics.CreateAPIView):
    """Create a new user type staff."""
    serializer_class = UserSerializer


class UserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user."""
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """Retrieve and return the authenticated user."""
        return self.request.user


class UserList(APIView):
    """
    List all users
    """
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class CreateClientView(generics.CreateAPIView):
    """Create a new client."""
    serializer_class = ClientSerializer


class ClentView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated client."""
    serializer_class = ClientSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """Retrieve and return the authenticated user."""
        return self.request.user


class ClientList(APIView):
    """
    List all clients
    """
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = ClientSerializer(users, many=True)
        return Response(serializer.data)