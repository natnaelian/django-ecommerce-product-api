# products/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path("", views.product_list_view, name="product-list"),
    path("<int:pk>/", views.product_detail_view, name="product-detail"),
    path("category/<str:category_name>/", views.category_filter_view, name="category-filter"),
]
