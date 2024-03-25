"""Offer methods urls"""


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OfferViewSet, OffersMatchView


router = DefaultRouter()
router.register('offer', OfferViewSet)
router.register('offer-match', OffersMatchView)


app_name = 'offers'

urlpatterns = [
    path('', include(router.urls)),
]