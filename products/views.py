# products/views.py
from rest_framework import generics, permissions, filters
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from .permissions import IsAdminOrReadOnly
from django.shortcuts import render


class ProductListCreateView(generics.ListCreateAPIView):
    """
    List all products or create a new product (admin only).
    """
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnly]
    queryset = Product.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'category__name']

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a product (update/delete = admin only).
    """
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnly]
    queryset = Product.objects.all()


class CategoryListView(generics.ListCreateAPIView):
    """
    List or create product categories (admin only for creation).
    """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [IsAdminOrReadOnly]

def product_list_view(request):
    products = Product.objects.all()
    return render(request, "products/product_list.html", {"products": products})


# 🔍 Product Detail View
def product_detail_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "products/product_detail.html", {"product": product})


# 🧭 Category Filter View
def category_filter_view(request, category_name):
    category = get_object_or_404(Category, name=category_name)
    products = Product.objects.filter(category=category)
    categories = Category.objects.all()
    return render(
        request,
        "products/category_filter.html",
        {"category": category, "products": products, "categories": categories}
    )
