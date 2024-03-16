from django.db import models

# Create your models here.
import uuid
from django.conf import settings
from offers.models import Offer
from payments.models import PaymentMethodUser


class TransactionStatus(models.Model):
    """Transaction status for transactions"""
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=100)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    """Model that describes the transaction (buy or sell)"""
    transaction_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    status = models.ForeignKey(
        TransactionStatus,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    source_offer_id = models.OneToOneField(
        Offer,
        on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s_source",
        blank=True,
        null=True
    )
    destination_offer_id = models.OneToOneField(
        Offer,
        on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s_destination",
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.transaction_id}'