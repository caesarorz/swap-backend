from django.db import models


class PaymentMethod(models.Model):
    """Payment methods in the system."""
    name = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    description = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    # objects = UserManager()

    # USERNAME_FIELD = 'email'

    def __str__(self):
        return self.name