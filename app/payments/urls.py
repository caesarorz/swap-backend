"""
Users urls
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PaymentMethodsViewSet

router = DefaultRouter()
router.register('payment-method', PaymentMethodsViewSet)


app_name = 'payments'

urlpatterns = [
    path('', include(router.urls)),
    # path('create/', PaymentMethodsViewSet.as_view(), name='create'),
]