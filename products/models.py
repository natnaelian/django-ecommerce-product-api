from django.db import models
from users.models import User

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        null=True,
        related_name="products"
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="products"
    )
    image = models.ImageField(
        upload_to='product_images/',  # Images saved in MEDIA_ROOT/product_images/
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
