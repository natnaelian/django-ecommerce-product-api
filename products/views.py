# products/views.py
from rest_framework import generics, permissions, filters
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from .permissions import IsAdminOrReadOnly


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
