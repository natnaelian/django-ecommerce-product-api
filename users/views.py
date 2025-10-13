# users/views.py
from rest_framework import generics, permissions
from .serializers import RegisterSerializer, UserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

# ✅ Registration View (already exists)
class RegisterView(generics.CreateAPIView):
    """
    Allows new users to register.
    """
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


# ✅ User Profile View
class UserProfileView(generics.RetrieveUpdateAPIView):
    """
    Allows authenticated users to view or update their profile information.
    """
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        # Returns the current logged-in user
        return self.request.user
