"""Payment methods urls"""


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PaymentMethodsViewSet, UserPaymentMethodsViewSet


router = DefaultRouter()
router.register('payment-method', PaymentMethodsViewSet)
router.register('user-payment-method', UserPaymentMethodsViewSet)


app_name = 'payments'

urlpatterns = [
    path('', include(router.urls)),
]