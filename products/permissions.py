# products/permissions.py
from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow only admin users to create, edit, or delete products.
    Everyone else can view (GET, HEAD, OPTIONS) only.
    """

    def has_permission(self, request, view):
        # SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS']
        if request.method in permissions.SAFE_METHODS:
            return True
        # Allow only staff/admin users for POST, PUT, DELETE
        return request.user and request.user.is_staff
