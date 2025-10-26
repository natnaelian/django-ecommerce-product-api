# users/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Custom user model extending Django's AbstractUser.

    Notes:
    - Email is unique and required.
    - Email is normalized to lowercase on save to avoid case-variant duplicates.
    - Ensure settings.AUTH_USER_MODEL = "users.User".
    """
    email = models.EmailField(
        unique=True,
        blank=False,
        null=False,
        help_text="User's email address (unique).",
    )

    def save(self, *args, **kwargs):
        # Normalize email to avoid case-sensitive duplicates
        if self.email:
            self.email = self.email.strip().lower()
        super().save(*args, **kwargs)

    def __str__(self):
        # Prefer username (default login) for display
        return self.username
