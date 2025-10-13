from rest_framework import serializers
from .models import Product, Category

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True
    )
    image = serializers.ImageField(required=False)  # ✅ allow optional image upload

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'description', 'price', 'stock',
            'category', 'category_id', 'created_by', 'created_at', 'updated_at',
            'image'
        ]
        read_only_fields = ['created_by', 'created_at', 'updated_at']
