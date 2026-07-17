from django.test import TestCase
from django.contrib.auth.models import User

from post.serializers import PostSerializer


class PostSerializerTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="admin",
            password="12345678"
        )

    def test_serializer_valid_data(self):

        data = {
            "title": "Django DRF",
            "content": "Bu content 10 ta belgidan uzun.",
        }

        serializer = PostSerializer(data=data)

        self.assertTrue(serializer.is_valid())

    def test_serializer_invalid_title(self):

        data = {
            "title": "      ",
            "content": "Bu content 10 ta belgidan uzun.",
        }

        serializer = PostSerializer(data=data)

        self.assertFalse(serializer.is_valid())
        self.assertIn("title", serializer.errors)

    def test_serializer_invalid_content(self):

        data = {
            "title": "Django",
            "content": "abc"
        }

        serializer = PostSerializer(data=data)

        self.assertFalse(serializer.is_valid())
        self.assertIn("content", serializer.errors)