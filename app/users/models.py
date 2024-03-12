""" Models for users: staff user model
    and clients users models
 """

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


USER_STATUS = (
    ('ACTIVE', 'active'),
    ('INACTIVE', 'inactive')
)

class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, email, phone_number, password=None, **extra_fields):
        """Create, save and return a new user."""
        if not email:
            raise ValueError('User must have an email address.')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(email, password)
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """Create and return a new superuser."""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False, blank=True, null=True)
    is_expert = models.BooleanField(default=False, blank=True, null=True)
    is_fraudulent = models.BooleanField(default=False, blank=True, null=True)
    rating = models.DecimalField(
        default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ],
        decimal_places=1,
        max_digits=2
     )
    status = models.CharField(max_length=20, choices=USER_STATUS, default='INACTIVE')
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)


    objects = UserManager()

    USERNAME_FIELD = 'email'
