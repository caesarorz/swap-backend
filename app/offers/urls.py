"""Offer methods urls"""


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OfferViewSet


router = DefaultRouter()
router.register('offer', OfferViewSet)


app_name = 'offers'

urlpatterns = [
    path('', include(router.urls)),
]