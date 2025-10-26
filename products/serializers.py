from rest_framework import serializers
from .models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source="category",
        write_only=True,
        allow_null=True,
        required=False,
    )
    image = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "description",
            "price",
            "stock",
            "category",
            "category_id",
            "created_by",
            "created_at",
            "updated_at",
            "image",
        ]
        read_only_fields = ["created_by", "created_at", "updated_at"]

    def validate_name(self, value: str) -> str:
        value = value.strip()
        if not value:
            raise serializers.ValidationError("Name cannot be blank.")
        return value

    def validate_description(self, value: str) -> str:
        return value.strip() if value is not None else value

    def create(self, validated_data):
        # created_by comes from the authenticated user (staff-only writes via permissions)
        request = self.context.get("request")
        if not request or not request.user or not request.user.is_authenticated:
            raise serializers.ValidationError("Authentication required.")
        validated_data["created_by"] = request.user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # Do not allow changing created_by via payload
        validated_data.pop("created_by", None)
        # Normalize strings
        if "name" in validated_data and validated_data["name"] is not None:
            validated_data["name"] = validated_data["name"].strip()
        if "description" in validated_data and validated_data["description"] is not None:
            validated_data["description"] = validated_data["description"].strip()
        return super().update(instance, validated_data)
