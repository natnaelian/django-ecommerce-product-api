# Django E‑Commerce Product API

Lightweight Django REST API for managing products and categories with optional HTML templates for basic product listing.

## Features
- Product CRUD endpoints (admin-only for writes) — see [`products.permissions.IsAdminOrReadOnly`](django-ecommerce-product-api/products/permissions.py).
- User registration and JWT authentication — see [`users.views.RegisterView`](django-ecommerce-product-api/users/views.py) and [`users.urls`](django-ecommerce-product-api/users/urls.py).
- Product image uploads, categories, created_by tracking — see [`products.models.Product`](django-ecommerce-product-api/products/models.py) and [`products.serializers.ProductSerializer`](django-ecommerce-product-api/products/serializers.py).
- Simple server-rendered product list and detail templates — see [products templates](django-ecommerce-product-api/products/templates/products/product_list.html), [product_detail.html](django-ecommerce-product-api/products/templates/products/product_detail.html), and [category_filter.html](django-ecommerce-product-api/products/templates/products/category_filter.html).

## Repository layout
- [django-ecommerce-product-api/manage.py](django-ecommerce-product-api/manage.py)
- [django-ecommerce-product-api/ecommerce/settings.py](django-ecommerce-product-api/ecommerce/settings.py)
- [django-ecommerce-product-api/ecommerce/urls.py](django-ecommerce-product-api/ecommerce/urls.py)
- [django-ecommerce-product-api/users/](django-ecommerce-product-api/users/)
  - [`users.views.RegisterView`](django-ecommerce-product-api/users/views.py)
  - [`users.views.UserProfileView`](django-ecommerce-product-api/users/views.py)
  - [django-ecommerce-product-api/users/serializers.py](django-ecommerce-product-api/users/serializers.py)
  - [django-ecommerce-product-api/users/models.py](django-ecommerce-product-api/users/models.py)
- [django-ecommerce-product-api/products/](django-ecommerce-product-api/products/)
  - [`products.views.ProductListCreateView`](django-ecommerce-product-api/products/views.py)
  - [`products.views.ProductDetailView`](django-ecommerce-product-api/products/views.py)
  - [django-ecommerce-product-api/products/models.py](django-ecommerce-product-api/products/models.py)
  - [django-ecommerce-product-api/products/serializers.py](django-ecommerce-product-api/products/serializers.py)
  - [django-ecommerce-product-api/products/permissions.py](django-ecommerce-product-api/products/permissions.py)
  - Templates: [product_list.html](django-ecommerce-product-api/products/templates/products/product_list.html)

## Requirements
Install dependencies from the project requirements:

```sh
pip install -r [requirements.txt](http://_vscodecontentref_/0)
```