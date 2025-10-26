# users/urls.py
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, UserProfileView, ChangePasswordView, LogoutView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("me/", UserProfileView.as_view(), name="me"),
    path("password/change/", ChangePasswordView.as_view(), name="password-change"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
