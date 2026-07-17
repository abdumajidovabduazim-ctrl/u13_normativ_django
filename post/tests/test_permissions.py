from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase


class PermissionTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="admin",
            password="12345678"
        )

    def test_anonymous_cannot_create_post(self):
        response = self.client.post(
            "/post-api/posts/",
            {
                "title": "Django",
                "content": "Bu content 10 ta belgidan uzun."
            },
            format="json"
        )

        self.assertIn(
            response.status_code,
            [
                status.HTTP_401_UNAUTHORIZED,
                status.HTTP_403_FORBIDDEN,
            ]
        )

    def test_authenticated_user_can_create_post(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.post(
            "/post-api/posts/",
            {
                "title": "Django",
                "content": "Bu content 10 ta belgidan uzun."
            },
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )