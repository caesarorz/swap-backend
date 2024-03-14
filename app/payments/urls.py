"""
Users urls
"""

from django.urls import path

from .views import PaymentMethodList

app_name = 'payments'

urlpatterns = [
    path('', PaymentMethodList.as_view(), name='list'),
    path('create/', PaymentMethodList.as_view(), name='create'),
]