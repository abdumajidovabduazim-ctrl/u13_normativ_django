from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase


class IntegrationTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="admin",
            password="12345"
        )

        response = self.client.post(
            "/api/token/",
            {
                "username": "admin",
                "password": "12345"
            },
            format="json"
        )

        print("STATUS:", response.status_code)
        print("BODY:", response.content)

        self.assertEqual(response.status_code, 200)

        self.token = response.json()["access"]

        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {self.token}"
        )

    def test_full_post_api(self):

        response = self.client.post(
            "/post-api/posts/",
            {
                "title": "Django DRF",
                "content": "Bu integration test uchun content."
            },
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        post_id = response.data["id"]

        response = self.client.get("/post-api/posts/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.put(
            f"/post-api/posts/{post_id}/",
            {
                "title": "Updated Django",
                "content": "Bu updated integration test content."
            },
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Updated Django")