"""Transaction methods urls"""


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TransactionViewSet


router = DefaultRouter()
router.register('transaction', TransactionViewSet)


app_name = 'transactions'

urlpatterns = [
    path('', include(router.urls)),
]