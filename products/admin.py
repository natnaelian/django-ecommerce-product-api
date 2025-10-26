from django.contrib import admin
from .models import Product, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "stock", "category", "created_by", "created_at")
    list_filter = ("category", "created_at")
    search_fields = ("name", "category__name", "created_by__username")
    autocomplete_fields = ("category",)
