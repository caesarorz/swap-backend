
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


class OffersMatchView(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = OfferSerializer
    queryset = Offer.objects.all()
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        """Retrive payment methods for authenticated users"""
        print("get_queryset", self.request.META)
        # if self.request.user.is_staff:
        return self.queryset.all().order_by('-id')
        # return self.queryset.filter(user=self.request.user).order_by('-id')

    def get_serializer_class(self):
        """Set serializer for actions detail or list"""
        print("get_serializer_class", self.request.data)

        # print(self.queryset.filter(user_payment_method_id=))

        # if self.action == 'list':
        #     return OfferSerializer
        return self.serializer_class

    # def get(self, request, format=None):
    #     """Get user payments"""
    #     print("get", request)
    #     user_payments = Offer.objects.all()
    #     serializer = OfferSerializer(user_payments, many=True)
    #     return Response(serializer.data)