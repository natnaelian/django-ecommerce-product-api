from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status

User = get_user_model()


class UsersFlowTests(APITestCase):
    def setUp(self):
        self.register_url = reverse("register")
        self.token_url = reverse("token_obtain_pair")
        self.refresh_url = reverse("token_refresh")
        self.me_url = reverse("me")
        self.change_password_url = reverse("password-change")
        self.logout_url = reverse("logout")

    def test_register_login_profile_change_password_logout(self):
        # Register
        payload = {
            "username": "alice",
            "email": "Alice@Example.com",
            "password": "StrongPass123!",
            "password2": "StrongPass123!",
        }
        r = self.client.post(self.register_url, payload, format="json")
        self.assertEqual(r.status_code, status.HTTP_201_CREATED, r.content)
        self.assertTrue(User.objects.filter(username="alice", email="alice@example.com").exists())

        # Login (JWT)
        r = self.client.post(self.token_url, {"username": "alice", "password": "StrongPass123!"}, format="json")
        self.assertEqual(r.status_code, status.HTTP_200_OK, r.content)
        access = r.data["access"]
        refresh = r.data["refresh"]

        # Profile (GET)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {access}")
        r = self.client.get(self.me_url)
        self.assertEqual(r.status_code, status.HTTP_200_OK)

        # Profile (PATCH) - change email
        r = self.client.patch(self.me_url, {"email": "new+Alice@Example.com"}, format="json")
        self.assertEqual(r.status_code, status.HTTP_200_OK)
        self.assertEqual(r.data["email"], "new+alice@example.com")

        # Change password
        r = self.client.post(self.change_password_url, {
            "old_password": "StrongPass123!",
            "new_password": "StrongerPass123!"
        }, format="json")
        self.assertEqual(r.status_code, status.HTTP_200_OK, r.content)

        # Login with new password
        r = self.client.post(self.token_url, {"username": "alice", "password": "StrongerPass123!"}, format="json")
        self.assertEqual(r.status_code, status.HTTP_200_OK)

        # Logout (blacklist refresh)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {access}")
        r = self.client.post(self.logout_url, {"refresh": refresh}, format="json")
        self.assertIn(r.status_code, (status.HTTP_204_NO_CONTENT, status.HTTP_200_OK))
