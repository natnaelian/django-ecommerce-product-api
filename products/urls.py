# products/urls.py

from django.urls import path
from .views import (
    ProductListCreateView,
    ProductDetailView,
    CategoryListView,
    product_list_view,
    product_detail_view,
    category_filter_view,
)

urlpatterns = [
    # API endpoints
    path("", ProductListCreateView.as_view(), name="product-list-create"),
    path("<int:pk>/", ProductDetailView.as_view(), name="product-detail"),
    path("categories/", CategoryListView.as_view(), name="category-list-create"),

    # Server-rendered HTML (optional)
    path("html/", product_list_view, name="product-list-html"),
    path("html/<int:pk>/", product_detail_view, name="product-detail-html"),
    path("html/category/<str:category_name>/", category_filter_view, name="category-filter-html"),
]
