# users/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Custom user model extending Django's AbstractUser.
    Adds optional fields for profile data in future if needed.
    """
    email = models.EmailField(unique=True)

    # You can add extra fields later like address, phone_number, etc.
    # phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username
