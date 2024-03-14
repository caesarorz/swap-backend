"""Database model for payment methods"""


from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

class PaymentMethod(models.Model):
    """Payment methods in the system."""
    name = models.CharField(max_length=100, unique=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    is_active = models.BooleanField(default=True)
    description = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)


    def __str__(self):
        return self.name