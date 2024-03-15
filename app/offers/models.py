from django.db import models

# Create your models here.
import uuid
from django.conf import settings
from django.contrib.auth import get_user_model
from payments.models import PaymentMethodUser




OFFER_TYPES = [('buy', 1), ('sell', 2)]

class Offer(models.Model):
    """Model that describes the offer (buy or sell)"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    user_payment_method_id = models.ForeignKey(PaymentMethodUser, on_delete=models.CASCADE)
    amount = models.PositiveSmallIntegerField(blank=False)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    offer_type = models.CharField(choices=OFFER_TYPES, default=OFFER_TYPES[0], max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'user_payment {self.user_payment_method_id} - type: {self.offer_type}'

