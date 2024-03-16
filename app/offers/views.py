
from rest_framework import (
    viewsets,
    mixins,
    status,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.settings import api_settings
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Offer
from .serializers import OfferSerializer

class OfferViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    """View for managing offers APIs
    """
    serializer_class = OfferSerializer
    queryset = Offer.objects.all()
    authentication_classes = [JWTAuthentication]